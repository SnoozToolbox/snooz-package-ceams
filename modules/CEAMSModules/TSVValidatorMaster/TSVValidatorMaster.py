"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    TSVValidatorMaster
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os
import pandas as pd

DEBUG = False

class TSVValidatorMaster(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        files: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        output_logs: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module TSVValidatorMaster """
        super().__init__(**kwargs)
        if DEBUG: print('TSVValidatorMaster.__init__')

         # The iteration over a list of files is not complete yet
        self.is_done = False
        # Allow iteration over a list of files
        self.is_master = True
        # Input plugs
        InputPlug('files',self)
        InputPlug('log_path',self)

        # Output plugs
        OutputPlug('output_logs',self)
        
    
    def compute(self, files, log_path):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            files: TODO TYPE
                TODO DESCRIPTION
            log_path: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            output_logs: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('TSVValidatorMaster.compute')
        # Check if the input is valid. This is done by checking the type of the input.
        # If the input is not valid, raise a NodeInputException. This will stop the process
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None    

        if files == '' or files is None or len(files) == 0:
            raise NodeInputException(self.identifier, "files", \
                "TSV Validator input files parameter must be set.")
        
        filename = files[self._iteration_counter]

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename

        if self._iteration_counter + 1 >= len(files):
            self.is_done = True

        if filename is not None:
            errors = []

            # Generate log path based on file name
            base_name = os.path.basename(filename)
            name_without_ext = os.path.splitext(base_name)[0]
            log_file_path = f"{log_path}{name_without_ext}_validation_log.txt"

            # UTF-8 check
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    f.read()  # Just try reading to verify encoding
                    print(f"File '{filename}' is UTF-8 encoded.")
            except UnicodeDecodeError:
                errors.append("File encoding is not UTF-8.")
                with open(log_file_path, 'w') as log_file:
                    for error in errors:
                        log_file.write(error + '\n')
                print(f"Validation failed. Encoding issue found. See '{os.path.abspath(log_file_path)}'.")
                return False

            try:
                # Read the TSV file
                df = pd.read_csv(filename, sep='\t', encoding='utf-8')

                # Define the expected columns
                expected_columns = ['group', 'name', 'start_sec', 'duration_sec', 'channels']

                # Check 1: Columns must match exactly
                if list(df.columns) != expected_columns:
                    errors.append(f"Column mismatch. Expected {expected_columns}, but got {list(df.columns)}")
                
                # Check 2: Validate each row's content
                for idx, row in df.iterrows():
                    if not isinstance(row['group'], str):
                        errors.append(f"Row {idx}: 'group' should be str, got {type(row['group']).__name__}")
                    if not isinstance(row['name'], (str, int)):
                        errors.append(f"Row {idx}: 'name' should be int or str, got {type(row['name']).__name__}")
                    if not isinstance(row['start_sec'], (float, int)):
                        errors.append(f"Row {idx}: 'start_sec' should be float or int, got {type(row['start_sec']).__name__}")
                    if not isinstance(row['duration_sec'], (float, int)):
                        errors.append(f"Row {idx}: 'duration_sec' should be float or int, got {type(row['duration_sec']).__name__}")
                    if not isinstance(row['channels'], str):
                        errors.append(f"Row {idx}: 'channels' should be str, got {type(row['channels']).__name__}")

            except Exception as e:
                errors.append(f"File could not be read or processed: {str(e)}")

            # Write all errors to a log file
            if errors:
                with open(log_file_path, 'w') as log_file:
                    log_file.write("Validation failed. Issues found:\n")
                    for error, item in zip(errors, range(len(errors))):
                        log_file.write(f"{item+1}: {error}\n")
                print(f"Validation failed. Details are saved in '{os.path.abspath(log_file_path)}'.")
            else:
                with open(log_file_path, 'w') as log_file:
                    log_file.write("Validation successful. No issues found.")

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'output_logs': None
        }