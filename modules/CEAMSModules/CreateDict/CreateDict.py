"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    CreateDict
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CreateDict(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        Key: TODO TYPE
            TODO DESCRIPTION
        Value: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        Dict: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module CreateDict """
        super().__init__(**kwargs)
        if DEBUG: print('CreateDict.__init__')

        # Input plugs
        InputPlug('Key',self)
        InputPlug('Value',self)
        

        # Output plugs
        OutputPlug('Dict',self)
        OutputPlug('Value',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, Key,Value):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            Key: TODO TYPE
                TODO DESCRIPTION
            Value: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            Dict: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('CreateDict.compute')
        Dictionary = {Key:Value}

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a dictionary.")

        return {
            'Dict': str(Dictionary), 
            'Value': Value
        }