#! /usr/bin/env python3
"""
    InputFiles
    Step to open files to convert REMs into  mini-epochs.
"""

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep

class InputFiles( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")

    psg_reader_identifier = "9168dcad-ee1b-4b56-ba71-6836188d1609"
    valid_stage_mandatory   = False     # To verify that all recordings have valid sleep stages
    valid_selected_chan     = False     # To verify if at leas one chan is selected for each file
    valid_single_chan       = False     # To verify if only one chan is selected for each file

    """
        InputFiles
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform PSGReader of the files to open and propagate the events included in the files.
    """

# For the other functions see CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep