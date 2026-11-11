"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    LempZivComplexityDoc
    Description of the columns of the cohort report written by the
    LempZivComplexity module.

    The dictionary returned by _get_doc is used twice :
        - to write the "_info" file next to the cohort report, so the user
          knows what each column means;
        - to order the columns of the cohort report, so the report and the
          "_info" file always describe the same columns in the same order.
"""
import csv


def write_doc_file(filepath):
    """ Write the description of each column of the cohort report.

    Each line of the file holds the letter of the column (as shown in Excel),
    the name of the column and its description.
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')
        doc = _get_doc()
        for i, (k, v) in enumerate(doc.items()):
            row_name = excel_column_name(i+1)
            docwriter.writerow([row_name, k, v])


def excel_column_name(number):
    """ Convert a column number (1, 2, ... 27) into an Excel name (A, B, ... AA). """
    column_name = ""
    while number > 0:
        remainder = (number - 1) % 26  # Subtract 1 to account for 0-based indexing
        column_name = chr(65 + remainder) + column_name  # 65 is the ASCII code for 'A'
        number = (number - 1) // 26
    return column_name


def _get_doc():
    """ Return the columns of the cohort report and their description. """
    return \
    {
        'filename' : 'PSG filename',
        'id1' : 'subject identification',
        'mode' : 'Complexity mode : "univariate" (one value per channel), '\
            '"joint" (Zozor joint LZC across channels) or "concat" (Schartner concatenation of the channels).',
        'channel' : 'The label of the channel in the univariate mode. "all" in the joint and concat modes, '\
            'the value is then computed on all the channels listed in the column "channels".',
        'n_channels' : 'The number of channels used to compute the complexity.',
        'channels' : 'The labels of the channels used to compute the complexity (separated by ";").',
        'sample_rate' : 'The sampling rate (Hz) of the channels.',
        'epoch_length_sec' : 'The length in sec of the epochs on which the complexity is computed.',
        'n_epochs_total' : 'The number of epochs extracted from the selected sleep stages or annotations.',
        'n_epochs_kept' : 'The number of epochs analysed (epochs without artefact).',
        'n_epochs_rejected' : 'The number of epochs rejected because they contain an artefact '\
            '(excluded event) or a flat signal on at least one channel.',
        'average_lzc' : 'The mean of the normalized Lempel-Ziv complexity over the analysed epochs.',
        'std_lzc' : 'The standard deviation of the normalized Lempel-Ziv complexity over the analysed epochs.',
        'median_lzc' : 'The median of the normalized Lempel-Ziv complexity over the analysed epochs.',
        'min_lzc' : 'The minimum normalized Lempel-Ziv complexity over the analysed epochs.',
        'max_lzc' : 'The maximum normalized Lempel-Ziv complexity over the analysed epochs.',
    }
