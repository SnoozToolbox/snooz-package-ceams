"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    This step is used to select the files for complexity analysis.
"""

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep


class InputFilesCplxStep(InputFilesStep):

    # Overwrite the default values of the base class
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "fee6b1f2-3ca8-498b-8ea2-8f8159f1b927"
    valid_stage_mandatory = False    # Complexity can run on unscored data
    valid_selected_chan   = True     # At least one channel must be selected
    valid_single_chan     = False    # Multiple channels are allowed

    """
        InputFilesCplxStep
        This step is used to select the files for EEG complexity analysis.
    """
