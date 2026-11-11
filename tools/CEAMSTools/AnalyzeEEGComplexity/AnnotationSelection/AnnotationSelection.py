#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    AnnotationSelection
    Step to select annotations for the Complexity analysis (same pattern as Connectivity).
"""

from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep
from CEAMSTools.AnalyzeEEGComplexity.FilterStep.FilterStep import FilterStep


class AnnotationSelection(NonValidEventStep):
    """
        AnnotationSelection
        Publishes selected annotation group/name dictionaries to SignalsFromEvents
        when the analysis scope is specific_annotations. For sleep stages / unscored,
        publishes empty dictionaries so SignalsFromEvents keeps all received events.
    """

    # Not used for annotation cropping (Events Exclusion owns ResetSignalArtefact)
    node_id_ResetSignalArtefact_0 = None

    # Annotation Dictionaries in AnalyzeEEGComplexity.json
    node_id_Dictionary_group = "153a5e48-5cf0-4a36-abc6-6e3d5b6d0c39"  # events_groups
    node_id_Dictionary_name = "bb68afb9-b518-466d-99cf-d641612118d5"   # events_names

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.reset_excl_event_checkBox.setEnabled(False)

        # Annotation-branch SignalsFromEvents in AnalyzeEEGComplexity.json
        self._node_id_SignalsFromEvents = "d322fe3a-7e09-474b-aee5-9f202836dee4"
        self.sleep_stage_scope = False
        self.annot_selection_scope = False
        self.enable_widgets(False)
        self.match_event_channels_checkBox.setChecked(True)

    def on_apply_settings(self):

        if self.annot_selection_scope:
            # Specific annotations: publish the user-selected group/name dicts so
            # SignalsFromEvents crops the signal on those annotations.
            super().on_apply_settings()
        else:
            # Sleep stages OR unscored: publish empty group/name dicts.
            # For the sleep branch, SleepStageEvents has already filtered the events
            # to the selected stages, and SignalsFromEvents keeps ALL received
            # events when events_groups == ''. Empty strings (not None) also avoid
            # the downstream None.split() crash.
            files_list = self.reader_settings_view.get_files_list(self.files_check_event_model)
            empty_dict = {file: "" for file in files_list}
            self._pub_sub_manager.publish(self, self._artefact_group_topic, str(empty_dict))
            self._pub_sub_manager.publish(self, self._artefact_name_topic, str(empty_dict))

    def load_settings(self):
        super().load_settings()
        # Sync the scope from the context (it may have been set by FilterStep
        # before this step subscribed to the context manager).
        self._sync_scope_from_context()
        # Ping activation state of the annotation-branch SignalsFromEvents
        self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents+".get_activation_state", None)

    def _sync_scope_from_context(self):
        try:
            scope = self._context_manager[FilterStep.context_Con_scope]
        except (KeyError, TypeError):
            scope = "sleep_stages"
        self.annot_selection_scope = (scope == "specific_annotations")
        self.sleep_stage_scope = (scope == "sleep_stages")
        # Only enable the annotation selection widgets for the annotation scope.
        self.enable_widgets(self.annot_selection_scope)

    def on_topic_update(self, topic, message, sender):
        """Called when context or other topics update."""
        super().on_topic_update(topic, message, sender)

        if topic == self._context_manager.topic:
            # The analysis scope changed in FilterStep.
            if message == FilterStep.context_Con_scope:
                self._sync_scope_from_context()

    def on_topic_response(self, topic, message, sender):
        super().on_topic_response(topic, message, sender)

    def enable_widgets(self, bool_flag):
        self.file_listview.setEnabled(bool_flag)
        self.event_treeview.setEnabled(bool_flag)
        self.select_all_checkBox.setEnabled(False)
        self.search_lineEdit.setEnabled(bool_flag)
        self.reset_all_files_pushButton.setEnabled(bool_flag)
