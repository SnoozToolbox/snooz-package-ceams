"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

LempZivComplexity
-----------------
Compute the Fourier-surrogate normalized Lempel-Ziv complexity (FJZC) of EEG
epochs, following Toker et al. (PNAS 2022).

The module accepts the epochs of every channel (Epoch Signal), rejects the
epochs contaminated by artefacts (NaN, Inf or flat zeros, as the connectivity
modules do), computes the complexity of the remaining epochs and summarizes it
over the recording.

The results are returned on the lzc_results output plug, so that another
module can use them, and they are written on disk the same way as the PSA
and the spindle tools do :

    Cohort report (cohort_filename)
        A single TSV file for the whole cohort. Each recording appends its
        lines at the end of the file : one line per recording in the joint and
        concat modes, one line per recording and channel in the univariate
        mode. The header is written only when the file is created, and a
        "<cohort>_info.tsv" file describing the columns is written next to it.
        Running the tool again with the same file adds new lines to it.

    Detailed tables (export_details)
        One file per recording, named after the recording :
            <recording>_lzc_<mode>_per_epoch.tsv : one line per epoch.
            <recording>_lzc_univariate_per_epoch_per_channel.tsv : the epoch
                by channel table, univariate mode only.
        They are written in the "complexity_details" folder next to the
        cohort report, or next to the recording when no cohort report is
        defined.

Inputs:
    recording_path : str
        Recording file, used to name the detailed tables when the PSG Reader
        information is missing and to find the folder of the recording.
    subject_info : dict
        Information from the PSG Reader, 'filename' and 'id1' are written in
        the output files to identify the recording.
    epochs : list of EpochModel
        One EpochModel per channel, as created by the Epoch Signal module.
    events : pandas.DataFrame
        Events used to select the data (sleep stages or annotations). Each
        epoch is labelled with the event it falls into.
    mode : str
        'joint' (Zozor), 'concat' (Schartner) or 'univariate' (per channel).
    cohort_filename : str
        Path of the cohort report (.tsv). Empty means no cohort report.
    export_details : bool or str
        True to write the detailed tables of each recording.

Outputs:
    lzc_results : dict
        Complexity values, epoch information and list of the written files.
"""

import os

import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.LempZivComplexity.FJZC_utils import FJZC_parallel
from CEAMSModules.LempZivComplexity.LempZivComplexityDoc import write_doc_file, _get_doc

DEBUG = False

VALID_MODES = ('joint', 'concat', 'univariate')

# Number of channels above which the joint mode saturates (see FJZC_utils).
JOINT_CHANNEL_WARNING_LIMIT = 50

# Folder created next to the cohort report to hold the detailed tables.
DETAILS_FOLDER_NAME = 'complexity_details'


def _to_bool(value):
    """ Convert the export flag received from the interface ('True', 'False', 1, ...). """
    if isinstance(value, str):
        return value.strip().lower() in ('true', '1', 'yes')
    return bool(value)


def _subject_base(subject_info, recording_path):
    """
    Return the recording name used as a prefix for the output files.

    The PSG Reader already provides the filename without path and extension.
    The recording path is the fallback when the module is used without reader.
    """
    if isinstance(subject_info, dict) and subject_info.get('filename'):
        return str(subject_info['filename'])
    if recording_path and str(recording_path).strip():
        return os.path.splitext(os.path.basename(str(recording_path).strip()))[0]
    return 'lzc'


def _subject_columns(subject_info, recording_path):
    """
    Return the columns identifying the recording in every output file.

    The same first columns as the PSA compilation files are used, so the
    results of many recordings can be appended into a single table.
    """
    identifier = ''
    if isinstance(subject_info, dict):
        for key in ('id1', 'id2'):
            value = subject_info.get(key)
            if value is not None and str(value).strip():
                identifier = str(value).strip()
                break
    return {
        'filename': _subject_base(subject_info, recording_path),
        'id1': identifier,
    }


def _epoch_time_vectors(epochs, n_epochs):
    """
    Return the start and the end time (sec) of every epoch of the recording.

    The Epoch Signal module stores those times in each EpochModel, they are
    identical for all channels, the first channel is therefore enough. NaN is
    returned when the times are not available, the output files then only
    hold the epoch index.
    """
    start_sec = np.full(n_epochs, np.nan, dtype=np.float64)
    end_sec = np.full(n_epochs, np.nan, dtype=np.float64)
    start_list = getattr(epochs[0], 'start_time', None)
    end_list = getattr(epochs[0], 'end_time', None)
    if start_list is not None and len(start_list) == n_epochs:
        start_sec = np.asarray(start_list, dtype=np.float64)
    if end_list is not None and len(end_list) == n_epochs:
        end_sec = np.asarray(end_list, dtype=np.float64)
    return start_sec, end_sec


def _label_epochs(events, start_sec, end_sec):
    """
    Return the group and the name of the event covering each epoch.

    The events are the ones used to select the data : the sleep stages for the
    sleep stage scope and the annotations for the annotation scope. Labelling
    each epoch allows the user to know which stage or annotation the
    complexity value comes from. An empty label means that no event covers
    the epoch, which happens on the unscored recording.
    """
    n_epochs = len(start_sec)
    group = np.full(n_epochs, '', dtype=object)
    name = np.full(n_epochs, '', dtype=object)

    if not isinstance(events, pd.DataFrame) or events.empty:
        return group, name
    if not {'start_sec', 'duration_sec'}.issubset(events.columns):
        return group, name

    event_start = events['start_sec'].to_numpy(dtype=np.float64)
    event_end = event_start + events['duration_sec'].to_numpy(dtype=np.float64)
    groups = events['group'].to_numpy() if 'group' in events.columns else None
    names = events['name'].to_numpy() if 'name' in events.columns else None

    for i_epoch in range(n_epochs):
        start = start_sec[i_epoch]
        if not np.isfinite(start):
            continue
        end = end_sec[i_epoch]
        # The middle of the epoch identifies the event without ambiguity when
        # the epochs overlap the border of two consecutive events.
        middle = (start + end) / 2.0 if np.isfinite(end) else start
        covering = np.flatnonzero((event_start <= middle) & (middle < event_end))
        if covering.size == 0:
            continue
        i_event = covering[0]
        if groups is not None:
            group[i_epoch] = str(groups[i_event])
        if names is not None:
            name[i_epoch] = str(names[i_event])
    return group, name


def _lzc_statistics(lzc_values):
    """ Return the statistics of the complexity over the analysed epochs. """
    lzc_values = np.asarray(lzc_values, dtype=np.float64)
    return {
        'average_lzc': float(np.nanmean(lzc_values)),
        'std_lzc': float(np.nanstd(lzc_values)),
        'median_lzc': float(np.nanmedian(lzc_values)),
        'min_lzc': float(np.nanmin(lzc_values)),
        'max_lzc': float(np.nanmax(lzc_values)),
    }


def _cohort_report_df(lzc_results, subject_cols):
    """
    Return the lines of the recording to append to the cohort report.

    The joint and concat modes give a single value per epoch for all the
    channels together, the recording is then described by one line where
    the channel is "all". The univariate mode gives one value per epoch and
    per channel, the recording is then described by one line per channel,
    as the PSA report does. The columns are ordered as in the "_info" file.
    """
    channel_names = list(lzc_results['channel_names'])
    # Information shared by all the lines of the recording.
    recording_info = dict(subject_cols)
    recording_info.update({
        'mode': lzc_results['mode'],
        'n_channels': len(channel_names),
        # Semicolon separated since the channel labels often contain spaces.
        'channels': ';'.join(channel_names),
        'sample_rate': lzc_results['sample_rate'],
        'epoch_length_sec': lzc_results['epoch_length_sec'],
        'n_epochs_total': lzc_results['n_epochs_total'],
        'n_epochs_kept': lzc_results['n_epochs_kept'],
        'n_epochs_rejected': lzc_results['n_epochs_rejected'],
    })

    rows = []
    per_epoch_per_channel = lzc_results.get('per_epoch_per_channel_lzc')
    if per_epoch_per_channel is not None:
        # Univariate mode : one column of the matrix per channel.
        per_epoch_per_channel = np.asarray(per_epoch_per_channel, dtype=np.float64)
        for i_chan, channel in enumerate(channel_names):
            row = dict(recording_info)
            row['channel'] = channel
            row.update(_lzc_statistics(per_epoch_per_channel[:, i_chan]))
            rows.append(row)
    else:
        row = dict(recording_info)
        row['channel'] = 'all'
        row.update(_lzc_statistics(lzc_results['per_epoch_lzc']))
        rows.append(row)

    return pd.DataFrame(rows)[list(_get_doc().keys())]


def _details_tables(lzc_results, per_epoch_df):
    """
    Return the detailed tables of the recording as {suffix: DataFrame}.

    The per epoch table is always returned. The epoch by channel table only
    exists in the univariate mode, it holds the epoch index and the start
    time so that each line can be matched with the per epoch table.
    """
    tables = {'per_epoch': per_epoch_df}
    per_epoch_per_channel = lzc_results.get('per_epoch_per_channel_lzc')
    if per_epoch_per_channel is not None:
        matrix_df = pd.DataFrame(
            np.asarray(per_epoch_per_channel, dtype=np.float64),
            columns=list(lzc_results['channel_names']),
        )
        matrix_df.insert(0, 'epoch_index', per_epoch_df['epoch_index'].to_numpy())
        matrix_df.insert(1, 'start_sec', per_epoch_df['start_sec'].to_numpy())
        tables['per_epoch_per_channel'] = matrix_df
    return tables


class LempZivComplexity(SciNode):
    """
    Normalized Lempel-Ziv complexity of EEG epochs.

    Parameters
    ----------
    epochs : list of EpochModel
        One EpochModel per channel, all channels must share the sampling
        frequency, the number of epochs and the epoch length.
    events : pandas.DataFrame
        Events used to select the data, used to label each epoch.
    mode : str
        'joint', 'concat' or 'univariate'. Empty means 'joint'.
    recording_path : str, optional
        Recording file, used to name the detailed tables when subject_info is
        missing and to write them next to the recording.
    subject_info : dict, optional
        Information from the PSG Reader, 'filename' and 'id1' are used.
    cohort_filename : str, optional
        Cohort report (.tsv) where the lines of the recording are appended.
        Empty means no cohort report.
    export_details : bool or str, optional
        True to write the detailed tables of the recording.

    Returns
    -------
    lzc_results : dict
        mode, channel_names, sample_rate, epoch_length_sec, epoch count and
        rejection count, complexity per epoch and averaged, complexity per
        channel for the univariate mode, the epoch table and the list of the
        files written on disk.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG:
            print('LempZivComplexity.__init__')

        InputPlug('recording_path', self)
        InputPlug('subject_info', self)
        InputPlug('epochs', self)
        InputPlug('events', self)
        InputPlug('mode', self)
        InputPlug('cohort_filename', self)
        InputPlug('export_details', self)

        OutputPlug('lzc_results', self)

        self._is_master = False

    def compute(self, epochs, events, mode, recording_path=None, subject_info=None,
                cohort_filename=None, export_details=None):
        """
        Compute the complexity of the epochs and write the TSV files.

        1. Validate the mode and the epochs.
        2. Reject the epochs contaminated by artefacts.
        3. Compute the normalized complexity of the remaining epochs.
        4. Label each epoch with the event it belongs to.
        5. Append the recording to the cohort report and write the detailed
           tables.
        """

        # -------------------------------------------------------------------
        # 1. Validate the inputs
        # -------------------------------------------------------------------
        # An empty mode happens when the module is used outside a tool, the
        # default of the module is then applied.
        if mode is None or (isinstance(mode, str) and mode.strip() == ''):
            mode = 'joint'
        if isinstance(mode, str):
            mode = mode.strip().lower()
        if mode not in VALID_MODES:
            raise NodeInputException(
                self.identifier, 'mode',
                f"'mode' must be one of {VALID_MODES}; got {mode!r}."
            )

        # The two checks on the epochs and on the sampling frequency depend on
        # the recording, they raise a NodeRuntimeException : the tool skips this
        # recording and continues with the next one of the cohort. A
        # NodeInputException would stop the analysis of all the recordings.
        if not epochs or len(epochs) == 0:
            raise NodeRuntimeException(
                self.identifier, 'epochs',
                'No epochs provided to LempZivComplexity.'
            )
        # No event is a valid situation, the unscored recording has none.
        if events is None:
            events = pd.DataFrame()
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(
                self.identifier, 'events',
                'Events must be a pandas DataFrame.'
            )

        # The complexity is computed on all channels at once, they must share
        # the same time base.
        fs_list = [float(e.sample_rate) for e in epochs]
        fs = fs_list[0]
        if not all(np.isclose(f, fs, rtol=0.0, atol=1e-9) for f in fs_list):
            per_channel_fs = ', '.join(
                f'{e.channel}: {f:g} Hz' for e, f in zip(epochs, fs_list))
            raise NodeRuntimeException(
                self.identifier, 'epochs',
                'All selected channels of a recording must share the same '
                f'sampling frequency. Got {per_channel_fs}. '
                'Select channels recorded at the same sampling frequency.'
            )

        shapes = [np.asarray(e.samples).shape for e in epochs]
        if not all(len(s) == 2 for s in shapes):
            raise NodeRuntimeException(
                self.identifier, 'epochs',
                f'Each EpochModel.samples must be 2D (W, T); got shapes: {shapes}'
            )
        n_epochs_total, n_samples = shapes[0]
        if any(s != (n_epochs_total, n_samples) for s in shapes):
            raise NodeRuntimeException(
                self.identifier, 'epochs',
                'All channels must have identical epoch count and epoch length. '
                f'Got shapes: {shapes}'
            )
        if n_samples < 2:
            raise NodeInputException(
                self.identifier, 'epochs',
                f'Epoch length (T) must be >= 2 samples; got {n_samples}.'
            )

        channel_names = [e.channel for e in epochs]
        n_channels = len(channel_names)
        epoch_length_sec = float(getattr(epochs[0], 'duration', n_samples / fs))

        # The joint mode packs all channels into a single symbol per sample,
        # the alphabet becomes too large for a dense montage (see FJZC_utils).
        joint_hd_warning = None
        if mode == 'joint' and n_channels > JOINT_CHANNEL_WARNING_LIMIT:
            joint_hd_warning = (
                f'WARNING: joint mode with {n_channels} channels often yields '
                f'normalized LZC ≈ 1 (joint-state saturation). Prefer '
                f"'univariate' for hd-EEG, or run joint on fewer channels."
            )
            print(f'[LempZivComplexity] {joint_hd_warning}', flush=True)
            self._log_manager.log(self.identifier, joint_hd_warning)

        # -------------------------------------------------------------------
        # 2. Reject the epochs contaminated by artefacts
        # -------------------------------------------------------------------
        # (n_epochs, n_channels, n_samples), the order of the channels is the
        # order of the epochs list and is kept for the whole module.
        windowed_signal = np.stack([e.samples for e in epochs], axis=1)
        if DEBUG:
            print(f'[LempZivComplexity] Shape before artifact removal: '
                  f'{windowed_signal.shape}')

        # Inf is treated as NaN, both mean that the sample is unusable.
        if not np.isfinite(windowed_signal).all():
            windowed_signal = windowed_signal.copy()
            windowed_signal[~np.isfinite(windowed_signal)] = np.nan

        # An epoch is rejected as soon as one channel holds a NaN, which is
        # the value written by Reset Signal Artefact on the excluded events.
        nan_epoch_mask = np.isnan(windowed_signal).any(axis=(1, 2))
        # A completely flat epoch carries no information and would bias the
        # surrogate normalization.
        zero_epoch_mask = (windowed_signal == 0).all(axis=(1, 2))
        valid_epochs = (~nan_epoch_mask) & (~zero_epoch_mask)
        clean_windowed_signal = windowed_signal[valid_epochs]

        n_epochs_kept = int(np.sum(valid_epochs))
        n_epochs_rejected = n_epochs_total - n_epochs_kept

        if n_epochs_kept == 0:
            raise NodeRuntimeException(
                self.identifier, 'ArtifactRemoval',
                'All epochs were rejected (NaN/Inf/zero). Nothing to compute.'
            )

        # -------------------------------------------------------------------
        # 3. Compute the normalized complexity
        # -------------------------------------------------------------------
        info = {
            'sampling_frequency': fs,
            'sample_rate': fs,
            'channel_names': channel_names,
        }

        try:
            fjzc_out = FJZC_parallel(
                clean_windowed_signal, info, mode=mode, n_jobs=-1
            )
        except OSError as e:
            raise NodeRuntimeException(
                self.identifier, 'ComplexityLibrary',
                f'Complexity library missing or not loadable: {e}'
            )
        except Exception as e:
            raise NodeRuntimeException(
                self.identifier, 'LZCComputation',
                f'Error in FJZC_parallel: {e}'
            )

        # -------------------------------------------------------------------
        # 4. Describe every analysed epoch
        # -------------------------------------------------------------------
        # Index of the analysed epochs within the whole recording, the
        # rejected ones are missing, the user can then see which epochs were
        # dropped instead of reading a renumbered table.
        kept_epoch_index = np.flatnonzero(valid_epochs)
        start_sec_all, end_sec_all = _epoch_time_vectors(epochs, n_epochs_total)
        event_group_all, event_name_all = _label_epochs(
            events, start_sec_all, end_sec_all)

        subject_cols = _subject_columns(subject_info, recording_path)
        per_epoch_lzc = np.asarray(fjzc_out['per_epoch_lzc'], dtype=np.float64)
        per_epoch_df = pd.DataFrame({
            'filename': subject_cols['filename'],
            'id1': subject_cols['id1'],
            'mode': mode,
            'epoch_index': kept_epoch_index,
            'start_sec': start_sec_all[kept_epoch_index],
            'end_sec': end_sec_all[kept_epoch_index],
            'duration_sec': epoch_length_sec,
            'event_group': event_group_all[kept_epoch_index],
            'event_name': event_name_all[kept_epoch_index],
            'lzc': per_epoch_lzc,
        })

        lzc_results = {
            'mode': mode,
            'channel_names': channel_names,
            'sample_rate': fs,
            'epoch_length_sec': epoch_length_sec,
            'n_epochs_total': n_epochs_total,
            'n_epochs_kept': n_epochs_kept,
            'n_epochs_rejected': n_epochs_rejected,
            'kept_epoch_index': kept_epoch_index,
            'epoch_start_sec': start_sec_all[kept_epoch_index],
            'epoch_end_sec': end_sec_all[kept_epoch_index],
            'epoch_event_group': event_group_all[kept_epoch_index],
            'epoch_event_name': event_name_all[kept_epoch_index],
            'per_epoch_lzc': per_epoch_lzc,
            'average_lzc': fjzc_out['average_lzc'],
            # Filled for the univariate mode only, None for joint and concat.
            'per_epoch_per_channel_lzc': fjzc_out['per_epoch_per_channel_lzc'],
            'average_per_channel_lzc': fjzc_out['average_per_channel_lzc'],
            'per_epoch_table': per_epoch_df,
            'export_files': [],
        }

        # -------------------------------------------------------------------
        # 5. Write the results on disk
        # -------------------------------------------------------------------
        cohort_filename = str(cohort_filename).strip() if cohort_filename else ''
        export_details = _to_bool(export_details)
        export_files = []

        if cohort_filename:
            export_files += self._append_to_cohort_report(
                cohort_filename, _cohort_report_df(lzc_results, subject_cols))

        if export_details:
            export_files += self._write_details_tables(
                _details_tables(lzc_results, per_epoch_df), mode,
                _subject_base(subject_info, recording_path),
                cohort_filename, recording_path)

        lzc_results['export_files'] = export_files

        # Summary shown in the Results tab of the module.
        cache = {
            'mode': mode,
            'n_epochs_kept': n_epochs_kept,
            'n_epochs_rejected': n_epochs_rejected,
            'average_lzc': float(fjzc_out['average_lzc']),
            'channel_names': channel_names,
            'per_epoch_lzc_mean': float(np.mean(per_epoch_lzc)),
            'per_epoch_lzc_std': float(np.std(per_epoch_lzc)),
            'cohort_filename': cohort_filename,
            'export_files': export_files,
        }
        if joint_hd_warning:
            cache['warning'] = joint_hd_warning
        if mode == 'univariate' and fjzc_out['average_per_channel_lzc'] is not None:
            cache['average_per_channel_lzc'] = (
                fjzc_out['average_per_channel_lzc'].tolist()
            )
        try:
            self._cache_manager.write_mem_cache(self.identifier, cache)
        except Exception:
            pass

        # Message shown in the Logs tab.
        export_msg = (
            f'; {len(export_files)} file(s) written'
            if export_files else
            '; no file written (cohort_filename is empty and export_details is False)'
        )
        self._log_manager.log(
            self.identifier,
            f'LZC mode={mode}: kept {n_epochs_kept}/{n_epochs_total} epochs, '
            f'average_lzc={fjzc_out["average_lzc"]:.6g}'
            f'{export_msg}'
            + (f' | {joint_hd_warning}' if joint_hd_warning else '')
        )

        return {'lzc_results': lzc_results}

    def _append_to_cohort_report(self, cohort_filename, report_df):
        """
        Append the lines of the recording at the end of the cohort report.

        Same logic as the PSA report : the header is written only when the
        file does not exist yet, then each recording adds its lines. The
        "_info" file describing the columns is created with the report.
        Return the list of the files written.
        """
        written = []
        folder = os.path.dirname(cohort_filename)
        if folder and not os.path.isdir(folder):
            raise NodeRuntimeException(
                self.identifier, 'cohort_filename',
                f'The folder of the cohort report does not exist : {folder}')

        write_header = not os.path.exists(cohort_filename)
        try:
            report_df.to_csv(path_or_buf=cohort_filename, sep='\t',
                index=False, mode='a', header=write_header, encoding='utf_8')
        except Exception:
            raise NodeRuntimeException(
                self.identifier, 'cohort_filename',
                f'ERROR : Snooz can not write in the file {cohort_filename}. '
                'Check if the drive is accessible and ensure the file is not already open.')
        written.append(cohort_filename)

        # To write the info text file to describe the variable names
        if write_header:
            file_name, file_extension = os.path.splitext(cohort_filename)
            doc_filepath = file_name + '_info' + file_extension
            if not os.path.exists(doc_filepath):
                try:
                    write_doc_file(doc_filepath)
                except Exception:
                    raise NodeRuntimeException(
                        self.identifier, 'cohort_filename',
                        f'ERROR : Snooz can not write in the file {doc_filepath}. '
                        'Check if the drive is accessible and ensure the file is not already open.')
                written.append(doc_filepath)
                self._log_manager.log(self.identifier, f'The file {doc_filepath} has been created.')

        self._log_manager.log(self.identifier,
            f'{report_df["filename"].iloc[0]} is added to {cohort_filename}.')
        return written

    def _write_details_tables(self, tables, mode, base, cohort_filename, recording_path):
        """
        Write the detailed tables of the recording, one file per table.

        Same logic as the spindle details : the files go in a folder next to
        the cohort report so all the results of the cohort stay together.
        Without cohort report, they go next to the recording. The files are
        named after the recording and are replaced at each run.
        Return the list of the files written.
        """
        if cohort_filename:
            folder = os.path.join(os.path.dirname(cohort_filename), DETAILS_FOLDER_NAME)
        elif recording_path and str(recording_path).strip():
            folder = os.path.dirname(str(recording_path).strip())
        else:
            self._log_manager.log(self.identifier,
                'The detailed tables are not written, the folder of the '
                'recording and the cohort report are unknown.')
            return []

        written = []
        try:
            os.makedirs(folder, exist_ok=True)
            for suffix, table_df in tables.items():
                file_path = os.path.join(folder, f'{base}_lzc_{mode}_{suffix}.tsv')
                table_df.to_csv(path_or_buf=file_path, sep='\t',
                    index=False, mode='w', header=True, encoding='utf_8')
                written.append(file_path)
        except Exception:
            raise NodeRuntimeException(
                self.identifier, 'export_details',
                f'ERROR : Snooz can not write the detailed tables in the folder {folder}. '
                'Check if the drive is accessible and ensure the files are not already open.')

        self._log_manager.log(self.identifier,
            f'The detailed tables of {base} have been written in {folder}.')
        return written
