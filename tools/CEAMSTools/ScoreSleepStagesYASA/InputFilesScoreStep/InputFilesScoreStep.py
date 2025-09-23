"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.
"""

"""
    This step is used to select the files to score the sleep stages.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
#from AutomaticSleepScoringTools.AutomaticSleepScoring.InputFilesScoreStep.Ui_InputFilesScoreStep import Ui_InputFilesScoreStep
from commons.BaseStepView import BaseStepView

from widgets.WarningDialog import WarningDialog


class InputFilesScoreStep( InputFilesStep):

    # Overwrite the default values of the base class 
    # (really important to keep :
    #   context_files_view      = "input_files_settings_view")
    psg_reader_identifier = "031201d5-ff93-4be6-90d3-256d2ba689d1"
    valid_stage_mandatory = False    # To verify that all recordings have valid sleep stages
    valid_selected_chan   = True    # To verify if at least one channel is selected
    valid_single_chan     = False   # To verify if only one chan is selected for each file

    """
        InputFileStep
        This step is used to select the files to score the sleep stages.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Note: setupUi is already called in parent __init__, 
        # but we need to call it again for this specific UI
        # self.setupUi(self)  # Uncomment if this class has its own UI file
    
    # Get the alias values from PSGReaderSettingsView
    def get_aliases(self):
        """
        Get the alias values configured in the PSGReaderSettingsView.
        
        Returns
        -------
        dict
            Dictionary with alias names as keys and lists of channel names as values.
            Example: {'EOG': ['LOC-A2', 'ROC-A1'], 'EMG': ['Chin1-Chin2']}
        """
        if hasattr(self, 'my_PsgReaderSettingsView') and self.my_PsgReaderSettingsView is not None:
            return self.my_PsgReaderSettingsView.get_alias()
        else:
            return {}


    # Get channels for a specific alias
    def get_alias_channels(self, alias_name):
        """
        Get the list of channels for a specific alias.
        
        Parameters
        ----------
        alias_name : str
            Name of the alias (e.g., 'EOG', 'EMG', 'EEG')
            
        Returns
        -------
        list
            List of channel names for the specified alias, empty list if not found
        """
        aliases = self.get_aliases()
        return aliases.get(alias_name, [])
    

    def on_validate_settings(self):
        # Check alias configurations for EOG, EMG, and EEG
        all_aliases = self.get_aliases()
        eog_channels = self.get_alias_channels('EOG')
        emg_channels = self.get_alias_channels('EMG')
        eeg_channels = self.get_alias_channels('EEG')
                
        # Check if EEG alias is missing
        if all_aliases['EEG'] == ['']:
            WarningDialog(f"EEG alias is not configured. Please add an EEG alias for proper functioning of the algorithm.")
            return False
        
        # Check if EOG has more than one channel
        if len(eog_channels) > 1:
            WarningDialog(f"EOG alias has {len(eog_channels)} channels configured: {', '.join(eog_channels)}. "
                         f"Consider using only one EOG channel for proper functioning of the algorithm.")
            return False
        
        # Check if EMG has more than one channel  
        if len(emg_channels) > 1:
            WarningDialog(f"EMG alias has {len(emg_channels)} channels configured: {', '.join(emg_channels)}. "
                         f"Consider using only one EMG channel for proper functioning of the algorithm.")
            return False
        
        # Note: EEG can have multiple channels, so no check for multiple EEG channels
        
        # If alias validation passes, continue with parent validation
        return super().on_validate_settings()