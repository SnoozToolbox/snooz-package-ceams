"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    PSGReader reads a PSG file.

    Inputs:
        files -- Each file contains a montage and a list of channel to process.
        alias -- Channels alias to use for this process
    Ouputs:
        filename : string
            The name of the current PSG file.
        signals : List of SignalModel
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events list.
        sleep_stages : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Sleep stages list.
        subject_info : dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
        
"""
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

DEBUG = False

class PSGReader(SciNode):
    """
        PSGReader reads a PSG file.

        Inputs:
            files -- Each file contains a montage and a list of channel to process.
            alias -- Channels alias to use for this process
        Ouputs:
            filename : string
                The name of the current PSG file.
            signals : List of SignalModel
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Events list.
            sleep_stages : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Sleep stages list.
            subject_info : dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
            
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('PSGReader.__init__')
        self.is_done = False
        self.is_master = True
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()

        InputPlug('files', self)
        InputPlug('alias', self)
        OutputPlug('filename', self)
        OutputPlug('signals', self)
        OutputPlug('events', self)
        OutputPlug('sleep_stages', self)
        OutputPlug('subject_info', self)

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'PSGReader.on_topic_update {topic}:{message}')

    def get_next(self, files, filenames):
        filename = filenames[self.iteration_counter]
        if (not files[filename]==None) and ('montages' in files[filename]):
            montages = list(files[filename]['montages'].keys())

            for j in range(0, len(montages)):
                montage = montages[j]

                if files[filename]['montages'][montage]['is_selected']:
                    channels = files[filename]['montages'][montage]['channels']
                    selected_channels = [label for label in list(channels.keys()) if channels[label]['is_selected']]
                    montage_index = files[filename]['montages'][montage]['montage_index']

                    return filename, montage_index, selected_channels
        else:
            return filename, None, None

    def compute(self, files, alias):
        """
            Keyword arguments:
                files -- Each file contains a montage and a list of channel to process.
        """
        if DEBUG: print('PSGReader.compute')

        if files == '' or files is None or len(files) == 0:
            raise NodeInputException(self.identifier, "files", \
                "PSGReader files parameter must be set.")

        filenames = list(files.keys())
        filename, montage_index, selected_channels = self.get_next(files, filenames)

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename
        
        # Check if the file exist
        if(not os.path.isfile(filename)):
            raise NodeRuntimeException(self.identifier, "files", \
                f"PSGReader file not found:{filename}")

        # Try to open the file
        success = self._psg_reader_manager.open_file(filename)
        if not success:
            raise NodeRuntimeException(self.identifier, "files", \
                f"PSGReader could not read file:{filename}")
        
        signals = []
        if selected_channels is not None:
            signals = self.get_signal_models(selected_channels, montage_index, alias)    

        sleep_stages = self._psg_reader_manager.get_sleep_stages()
        events = self._psg_reader_manager.get_events()
        subject_info = self._psg_reader_manager.get_subject_info()

        # Write the events in the cache in order to view them on the resultsView
        if events is not None:
            cache = {}
            cache['events'] = events
            self._cache_manager.write_mem_cache(self.identifier, cache)

        self._psg_reader_manager.close_file()
        self._log_manager.log(self.identifier, f"{filename} has been read.")

        # Update progression information
        self.iteration_count = len(filenames)
        self.is_done = self.iteration_counter + 1 == len(filenames)

        return {
            'filename':filename,
            'signals':signals,
            'events':events,
            'sleep_stages':sleep_stages,
            'subject_info':subject_info
        }

    def get_alias(self, channel_name, alias):
        for alias_label in alias.keys():
            if channel_name in alias[alias_label]:
                return alias_label 

        return None

    def get_signal_models(self, selected_channels, montage_index, alias):
        signal_models = self._psg_reader_manager.get_signal_models(int(montage_index), selected_channels)

        for signal_model in signal_models:
            signal_model.alias = self.get_alias(signal_model.channel, alias)

        return signal_models