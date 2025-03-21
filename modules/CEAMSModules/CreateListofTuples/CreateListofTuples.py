"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    CreateListofTuples
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CreateListofTuples(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        events: TODO TYPE
            TODO DESCRIPTION
        group: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        events_to_remove: TODO TYPE
            TODO DESCRIPTION
        
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
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, events,group):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            events: TODO TYPE
                TODO DESCRIPTION
            group: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            events_to_remove: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if group == 'stage':
            events_to_remove = [(events['group'][i], events['name'][i]) for i, stage in enumerate(events['group']) if stage == 'stage']
        else:
            events_to_remove = []

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a list of tuples to remove unwanted events.")

        return {
            'events_to_remove': events_to_remove
        }