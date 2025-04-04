"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.

    CreateListofTuples
    A Flowpipe node that filters events based on group type and generates a list
    of tuples marking events for removal. Primarily used for sleep stage event processing.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd

DEBUG = False

class CreateListofTuples(SciNode):
    """
    Filters and transforms event data into a list of removable event tuples.
    When group='stage', creates tuples of (group, name) for each stage event.
    For other group types, returns an empty list.

    Parameters
    ----------
        events : pandas DataFrame
            Dictionary containing event data with 'group' and 'name' keys.
            Expected format: {'group': List[str], 'name': List[str]}
        group: str
            The group type to filter by (e.g., 'stage' for sleep stage events)

    Returns
    -------
        events_to_remove: List[Tuple[str, str]]
            List of (group, name) tuples for events matching the specified group
    """
    def __init__(self, **kwargs):
        """ Initialize module CreateListofTuples """
        super().__init__(**kwargs)
        if DEBUG: print('CreateListofTuples.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('group',self)
        

        # Output plugs
        OutputPlug('events_to_remove',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, events,group):
        """
        Processes event data and generates removal tuples based on group type.

        Parameters
        ----------
            events: pandas DataFrame
                Event data containing 'group' and 'name' lists
            group: str
                Target group type for filtering

        Returns
        -------
            events_to_remove: List[Tuple[str, str]]
                Filtered list of (group, name) tuples

        Raises
        ------
            NodeInputException
                If inputs are invalid (missing keys, wrong types)
            NodeRuntimeException
                If processing fails
        """
        if DEBUG: print('CreateListofTuples.compute')

        # Input validation
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", "Events must be a pandas DataFrame")
        if not all(key in events for key in ['group', 'name']):
            raise NodeInputException(self.identifier, "events", "Dictionary must contain 'group' and 'name' keys")
        if not isinstance(group, str):
            raise NodeInputException(self.identifier, "group", "Group must be a string")
        
        if group == 'stage':
            events_to_remove = [(events['group'][i], events['name'][i]) for i, stage in enumerate(events['group'])]
        else:
            events_to_remove = [(events['group'][i], events['name'][i]) for i, stage in enumerate(events['group']) if stage != 'stage']

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a list of tuples to remove unwanted events.")

        return {
            'events_to_remove': events_to_remove
        }