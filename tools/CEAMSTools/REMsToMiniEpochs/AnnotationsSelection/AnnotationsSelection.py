#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    AnnotationsSelection
    Class to send messages between step-by-step interface and plugins.
    Here we send the group and name of the annotations selected by the user for each filneame.
    Dictionary are used to store the information, the key is the filneame and
    values are the group or the name depending on the dict.
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class AnnotationsSelection(NonValidEventStep):
    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = None # reset the signal during annotation
    node_id_Dictionary_group = "b3ce9f72-36b1-4811-88f2-7899a8dfb7d0" # select the list of group for the current filename
    node_id_Dictionary_name = "97d9383b-9aad-45f3-aaf4-3e69fd0f0785" # select the list of name for the current filename    
    """
        AnnotationsSelection
        Class to send messages between step-by-step interface and plugins.
        Here we send the group and name of the annotations selected by the user for each filneame.
        Dictionary are used to store the information, the key is the filneame and
        values are the group or the name depending on the dict.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setEnabled(False)
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
