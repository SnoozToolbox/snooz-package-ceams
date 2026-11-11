"""
© 2025 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventCplxStep
    Step in the Complexity interface to exclude non valid events for the Complexity Analysis.
    The class is inherited from NonValidEventStep of PowerSpectralAnalysis.
        Doc to open and read to understand :
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep


class NonValidEventCplxStep(NonValidEventStep):
    """
    Events Exclusion for Complexity.

    The user checks events to exclude. On Apply, those group/name lists are
    stored per file in the two Dictionary nodes. ResetSignalArtefact is always
    activated and replaces the EEG samples during those events with NaN.
    Later epochs that contain those samples are dropped.

    The reset checkbox is locked on (same idea as Connectivity). The graph
    node uses signal_values = "NaN".
    """

    # ResetSignalArtefact in AnalyzeEEGComplexity.json (signal_values = NaN)
    node_id_ResetSignalArtefact_0 = "4fea5db4-0d6b-4c7f-94a6-e48e048bf677"
    # Dictionaries that look up artefact group/name for the current filename
    node_id_Dictionary_group = "f931825f-90fe-48a7-aa5c-fe3b08dcacfb"
    node_id_Dictionary_name = "64371bf1-f4c0-4f02-b65b-eb9226856939"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setChecked(True)
        self.reset_excl_event_checkBox.setEnabled(False)

# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
