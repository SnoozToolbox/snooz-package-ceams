"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the JsonPathEditorMaster plugin
"""

from qtpy import QtWidgets, QtCore, QtGui
import os
import re
import json

from CEAMSModules.JsonPathEditorMaster.Ui_JsonPathEditorMasterSettingsView import Ui_JsonPathEditorMasterSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog

DEBUG = False

class JsonPathEditorMasterSettingsView(BaseSettingsView, Ui_JsonPathEditorMasterSettingsView, QtWidgets.QWidget):
    """
        JsonPathEditorMasterView set the JsonPathEditorMaster settings
    """

    # To send a signal each time the self.files_model is modified
    # It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    model_updated_signal = QtCore.Signal()

    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        #setup the model
        self.files_model = QtGui.QStandardItemModel(0,1)
        self.Files_listView.setModel(self.files_model)

        self.Add_from_folders_pushButton.clicked.connect(self.on_add_folder)
        self.Add_files_pushButton.clicked.connect(self.on_add)
        #self.Remove_pushButton.clicked.connect(self.Files_listView.removeItemWidget)
        self.Remove_pushButton.clicked.connect(self.clear_list_slot)

        self.Files_listView.selectionModel().currentChanged.connect(self.on_file_selected)

        self.SelectAll_pushButton.clicked.connect(self.select_all_items)
        self.selectAll_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+A"), self)
        self.selectAll_shortcut.activated.connect(self.select_all_items)

        self.New_files_lineEdit.setPlaceholderText("Choose the folder that you want to save the new JSON files")
        self.Choose_pushButton.clicked.connect(self.select_save_folder)

        self.per_file_original_paths = {}  # key: file_path, value: list of original paths
        self.per_file_edited_paths = {}  # key: file_path, value: list of edited paths

        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)

        self._path_mapping_topic = f'{self._parent_node.identifier}.path_mapping'
        self._pub_sub_manager.subscribe(self, self._path_mapping_topic)

        self._newfilespath_topic = f'{self._parent_node.identifier}.newfilespath'
        self._pub_sub_manager.subscribe(self, self._newfilespath_topic)

        self._suffix_topic = f'{self._parent_node.identifier}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_topic)
    
    def validate_all_paths(self):
        """
        Validate paths only for the currently selected files.
        Returns a dictionary of file_path → missing original/edited paths.
        """
        missing_report = {}

        selected_indexes = self.Files_listView.selectedIndexes()
        selected_files = [self.files_model.data(index, QtCore.Qt.DisplayRole) for index in selected_indexes]

        for file_path in selected_files:
            originals = self.per_file_original_paths.get(file_path, [])
            edits = self.per_file_edited_paths.get(file_path, originals)  # fallback to original
            file_report = {
                "Missing Original Paths": [],
                "Missing Edited Paths": []
            }

            for old_path, new_path in zip(originals, edits):
                if not os.path.exists(old_path):
                    file_report["Missing Original Paths"].append(old_path)
                if not os.path.exists(new_path):
                    file_report["Missing Edited Paths"].append(new_path)

            if file_report["Missing Original Paths"] or file_report["Missing Edited Paths"]:
                missing_report[file_path] = file_report

        return missing_report

    def get_all_path_mappings(self):
        """
        Return a dictionary: {json_file_path: {original_path: edited_path, ...}, ...}
        Ensures edited paths from the current UI state are stored first.
        """
        path_mapping = {}

        # Save current table edits back to per_file_edited_paths
        if self.table_model and self.editable_model:
            edited_paths = [self.editable_model.item(row, 0).text() for row in range(self.editable_model.rowCount())]
            original_paths = [self.table_model.item(row, 0).text() for row in range(self.table_model.rowCount())]

            # Determine which files are currently selected in the list view
            selected_indexes = self.Files_listView.selectedIndexes()
            selected_files = [self.files_model.data(index, QtCore.Qt.DisplayRole) for index in selected_indexes]

            # Update each selected file with the latest edits
            for file_path in selected_files:
                # Match only the paths that belong to that file
                per_file_originals = self.per_file_original_paths.get(file_path, [])
                updated_edited_paths = []
                for orig in per_file_originals:
                    if orig in original_paths:
                        idx = original_paths.index(orig)
                        updated_edited_paths.append(edited_paths[idx])
                    else:
                        updated_edited_paths.append(orig)  # no edit shown, fallback to original

                self.per_file_edited_paths[file_path] = updated_edited_paths

        # Now build the mapping
        for file_path in selected_files:
            originals = self.per_file_original_paths.get(file_path, [])
            edits = self.per_file_edited_paths.get(file_path, originals)

            path_mapping[file_path] = {
                old: new for old, new in zip(originals, edits)
            }

        return path_mapping
    
    def select_save_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
           None, 
            'Select folder', 
            '', 
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if folder:
            if not folder.endswith('/') and not folder.endswith('\\'):
                folder += '/'
            self.New_files_lineEdit.setText(folder)

    def store_current_edits(self):
        """
        Save current edited paths (line by line) from the editable table view into per_file_edited_paths.
        """
        current_index = self.Files_listView.currentIndex()
        if not current_index.isValid() or not hasattr(self, 'editable_model'):
            return

        file_path = self.files_model.data(current_index, QtCore.Qt.DisplayRole)
        if not file_path:
            return

        edited_paths = [
            self.editable_model.item(row, 0).text()
            for row in range(self.editable_model.rowCount())
        ]
        self.per_file_edited_paths[file_path] = edited_paths

    def select_all_items(self):
        """
        Select all files and merge original/edited paths into a unified view.
        """
        selection_model = self.Files_listView.selectionModel()
        selection_model.clearSelection()

        # Save currently displayed edits (if any)
        self.store_current_edits()

        # Collect all unique original paths and their corresponding edited versions
        merged_originals = []
        merged_edits = []
        seen_paths = set()

        for row in range(self.files_model.rowCount()):
            index = self.files_model.index(row, 0)
            selection_model.select(index, QtCore.QItemSelectionModel.Select)

            file_path = self.files_model.data(index, QtCore.Qt.DisplayRole)

            if file_path not in self.per_file_original_paths:
                results = self.process_file(file_path)
                original_paths = [str(v) for _, v in results.items()]
                self.per_file_original_paths[file_path] = original_paths

            if file_path not in self.per_file_edited_paths:
                self.per_file_edited_paths[file_path] = list(self.per_file_original_paths[file_path])

            originals = self.per_file_original_paths[file_path]
            edits = self.per_file_edited_paths[file_path]

            for orig, edit in zip(originals, edits):
                if orig not in seen_paths:
                    seen_paths.add(orig)
                    merged_originals.append(orig)
                    merged_edits.append(edit)

        # Set up original paths model
        orig_model = QtGui.QStandardItemModel()
        orig_model.setHorizontalHeaderLabels(["Original Paths"])
        for path in merged_originals:
            item = QtGui.QStandardItem(path)
            item.setEditable(False)
            item.setForeground(QtGui.QBrush(QtGui.QColor('#888888')))
            orig_model.appendRow([item])
        self.Paths_tableView.setModel(orig_model)
        self.Paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Set up editable paths model
        edit_model = QtGui.QStandardItemModel()
        edit_model.setHorizontalHeaderLabels(["New Paths (To be edited)"])
        for orig, edit in zip(merged_originals, merged_edits):
            item = QtGui.QStandardItem(edit)
            item.setEditable(True)
            if edit == orig:
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
            elif not os.path.exists(edit):
                font = item.font()
                font.setBold(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('red')))
            edit_model.appendRow([item])

        self.New_paths_tableView.setModel(edit_model)

        self.table_model = orig_model
        self.editable_model = edit_model

    def clone_model_as_editable(self, source_model):
        editable_model = QtGui.QStandardItemModel()
        editable_model.setHorizontalHeaderLabels(["New Paths (To be edited)"])

        for row in range(source_model.rowCount()):
            value_item = source_model.item(row, 0).clone()
            # Mark value as editable
            value_item.setEditable(True)
            value_item.setForeground(QtGui.QBrush())
            editable_model.appendRow([value_item])

        return editable_model

    def collect_paths(self, obj, found_paths):
        """
        Recursively collect all unique folder paths from keys and values in the JSON structure.
        Handles both file and folder paths, and retains folders fully.
        """
        folder_set = set()

        def is_path(s):
            return isinstance(s, str) and re.match(r'^([A-Za-z]:|\\\\[^\\\/]+\\[^\\\/]+)[\\/]', s)

        def get_folder(s):
            s = s.replace('\\', '/')
            # Keep full path if no file extension
            if not re.search(r'\.[a-zA-Z0-9]{2,4}$', os.path.basename(s)):
                return s.rstrip('/')
            # Otherwise, return parent folder
            return os.path.dirname(s).replace('\\', '/')

        def recurse(item):
            if isinstance(item, dict):
                for k, v in item.items():
                    recurse(k)
                    recurse(v)
            elif isinstance(item, list):
                for sub in item:
                    recurse(sub)
            elif is_path(item):
                folder = get_folder(item)
                folder_set.add(folder)

        recurse(obj)
        found_paths.extend(sorted(folder_set))


    def on_file_selected(self, current, previous):
        if previous.isValid() and hasattr(self, 'editable_model'):
            prev_path = self.files_model.data(previous, QtCore.Qt.DisplayRole)
            self.per_file_edited_paths[prev_path] = [
                self.editable_model.item(row, 0).text()
                for row in range(self.editable_model.rowCount())
            ]

        if not current.isValid():
            return

        file_path = self.files_model.data(current, QtCore.Qt.DisplayRole)
        if not file_path:
            return

        # Re-process and store original paths
        results = self.process_file(file_path)
        original_paths = [str(value) for _, value in results.items()]
        self.per_file_original_paths[file_path] = original_paths

        # Always refresh original view
        orig_model = QtGui.QStandardItemModel()
        orig_model.setHorizontalHeaderLabels(["Original Paths"])
        for path in original_paths:
            item = QtGui.QStandardItem(path)
            item.setEditable(False)
            item.setForeground(QtGui.QBrush(QtGui.QColor('#888888')))
            orig_model.appendRow([item])
        self.Paths_tableView.setModel(orig_model)
        self.Paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_model = orig_model

        # Handle edited paths
        edited_paths = self.per_file_edited_paths.get(file_path, original_paths)
        if len(edited_paths) != len(original_paths):
            edited_paths = original_paths
            self.per_file_edited_paths[file_path] = edited_paths

        edit_model = QtGui.QStandardItemModel()
        edit_model.setHorizontalHeaderLabels(["New Paths (To be edited)"])
        for orig, edit in zip(original_paths, edited_paths):
            item = QtGui.QStandardItem(edit)
            item.setEditable(True)
            if edit == orig:
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
            elif not os.path.exists(edit):
                font = item.font()
                font.setBold(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('red')))
            edit_model.appendRow([item])

        self.New_paths_tableView.setModel(edit_model)
        self.editable_model = edit_model

    def process_file(self, file_path):
        # Example: if it's a JSON file, parse it
        #try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            found_paths = []
            self.collect_paths(data, found_paths)
            dict_paths = {path: found_paths[path] for path in range(len(found_paths))}
            return dict_paths
        '''except Exception as e:
            WarningDialog(f"Error! Could not read file:\n{e}")
            return {}'''
    
    # Slot called when user wants to add folders
    def on_add_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            'Select Folder Containing json Files',
            QtCore.QDir.homePath()
        )

        if folder_path:
            valid_extensions = ('json')
            file_list = [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith(valid_extensions)
            ]

            if not file_list:
               WarningDialog(f"No Valid Files. No json files found in the selected folder.")
               return

            for file_path in file_list:
                #self.Files_listView.addItem(file_path)
                # Later for better visualisation, we can only show the name of the file
                item = QtGui.QStandardItem(file_path)
                self.files_model.appendRow(item)

            self.model_updated_signal.emit()

    # Slot called when user wants to add files
    def on_add(self):
        filenames_add, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open json file', 
            None, 
            'JSON Files (*.json)')
        if filenames_add != '':
            # Fill the QListView
            for filename in filenames_add:
                #self.Files_listView.addItem(filename)
                # tree item : parent=file, child=name
                item = QtGui.QStandardItem(filename)
                self.files_model.appendRow(item) 
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 

    def load_files_from_data(self, data):
        self.files_model.clear()
        self.per_file_original_paths.clear()
        self.per_file_edited_paths.clear()
        self.Paths_tableView.setModel(None)
        self.New_paths_tableView.setModel(None)
        
        for filename in data:
            # Add files to listView
            item = QtGui.QStandardItem(filename)
            self.files_model.appendRow(item) 
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()

    def clear_list_slot(self):
        selected_indexes = self.Files_listView.selectedIndexes()
        if not selected_indexes:
            return

        # Get paths to remove
        paths_to_remove = [
            self.files_model.data(index, QtCore.Qt.DisplayRole)
            for index in selected_indexes
        ]

        # Remove from model (bottom-up)
        for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
            self.files_model.removeRow(index.row())

        # Remove from stored path dictionaries
        for path in paths_to_remove:
            self.per_file_original_paths.pop(path, None)
            self.per_file_edited_paths.pop(path, None)

        # Clear the table views if any displayed file is being deleted
        # Get the currently displayed file in table views
        current_index = self.Files_listView.currentIndex()
        current_file = None
        if current_index.isValid():
            current_file = self.files_model.data(current_index, QtCore.Qt.DisplayRole)

        # If current_file is missing or removed, clear the views
        if current_file is None or current_file in paths_to_remove:
            self.Paths_tableView.setModel(None)
            self.New_paths_tableView.setModel(None)
            self.table_model = None
            self.editable_model = None

        self.model_updated_signal.emit()


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._path_mapping_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._newfilespath_topic, 'ping')


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to JsonPathEditorMaster
        selected_indexes = self.Files_listView.selectedIndexes()

        '''if not selected_indexes:
           WarningDialog(f"No Selection", "Please select at least one file.")
           return'''

        selected_files = [self.files_model.data(index, QtCore.Qt.DisplayRole) for index in selected_indexes]
        # Send the full list to the backend
        self._pub_sub_manager.publish(self, self._files_topic, selected_files)

        self._pub_sub_manager.publish(self, self._path_mapping_topic, self.get_all_path_mappings())
        self._pub_sub_manager.publish(self, self._suffix_topic, str(self.Suffix_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._newfilespath_topic, str(self.New_files_lineEdit.text()))
        #self._pub_sub_manager.publish(self, self._newpaths_topic, str(self.newpaths_lineedit.text()))
        #self._pub_sub_manager.publish(self, self._newfilespath_topic, str(self.newfilespath_lineedit.text()))
        
        missing_paths = self.validate_all_paths()
        if missing_paths:
            # For example, log or show a warning
            print("Some paths are missing:", json.dumps(missing_paths, indent=2))

            WarningDialog(f"Some file paths do not exist. Please verify.\nDetails:\n{json.dumps(missing_paths, indent=2)}") # change it later in the tool
        else:
            print("All paths exist.")

    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if DEBUG: print(f'JsonPathEditorSettingsView.on_topic_response:{topic} message:{message}')
        if topic == self._files_topic:
            self.load_files_from_data(message)
        elif topic == self._suffix_topic:
            self.Suffix_lineEdit.setText(message)
        elif topic == self._newfilespath_topic:
            self.New_files_lineEdit.setText(message)


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._path_mapping_topic)
            self._pub_sub_manager.unsubscribe(self, self._suffix_topic)
            self._pub_sub_manager.unsubscribe(self, self._newfilespath_topic)  
