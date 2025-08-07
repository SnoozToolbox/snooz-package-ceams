"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtCore
""" 
    Model to placed between the files_check_event_model(QAbstractModel) and 
    the event_treeview (QTreeView) in order to filter groups.
    i.e. Filter the Tree viee to see only the artifacts via the search line edit "Comp".

    A custom model has been created to re-implement filterAcceptsRow.
    The default behavior of QSortFilterProxyModel is to filter the parent and 
    all the children.  EventsProxyModel only filters the events group 
    (not the filename and not the events name).
"""
class EventsProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filenames_filters = None
        self.group_search_pattern = None


    # source_row – PySide.QtCore.int, source_parent – PySide.QtCore.QModelIndex
    def filterAcceptsRow(self, sourceRow, sourceParent):
        #if self.filenames_filters is not None :
        # index(int row, int column, const QModelIndex &parent = QModelIndex())
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent) # string (filename, group, name)
        index1 = self.sourceModel().index(sourceRow, 1, sourceParent) # count useless
        item = self.sourceModel().itemFromIndex(index0)
        cur_text = self.sourceModel().data(index0)
        cur_count = self.sourceModel().data(index1)
        #print(f"all row:{sourceRow} : text={cur_text} and count={cur_count}")
        if ((item is not None) and item.hasChildren()) and (item.parent() is not None):
            # Group
            #print(f"group row:{sourceRow} : text={cur_text} and count={cur_count}")
            if self.group_search_pattern is not None:
                return self.group_search_pattern in cur_text
            else:
                return True
        # Name or filename
        else:
            return True


    def set_filenames_filters(self, filenames):
        self.filenames_filters = filenames
        self.invalidate()
    

    def set_groups_search_pattern(self, pattern):
        self.group_search_pattern = pattern
        self.invalidate()


    @property
    def selection(self):
        return self._selection
    
    
    @selection.setter
    def selection(self, value):
        self._selection = value

    def count_checked_items_cohort(self):
        def count_checked_recursive(item):
            name_checked = 0
            group_checked = 0
            for row in range(item.rowCount()):
                child = item.child(row)
                if child.isCheckable() and child.checkState() == QtCore.Qt.Checked:
                    if not child.hasChildren() and (not child in childlist):
                        name_checked += 1
                        childlist.append(child.text())
                    if child.hasChildren() and (not child in childlist):
                        group_checked += 1
                        childlist.append(child.text())
                # Recurse into deeper levels if needed
                child_name_checked, child_group_checked = count_checked_recursive(child)
                name_checked += child_name_checked
                group_checked += child_group_checked
            return name_checked, group_checked

        total_name_checked = 0
        total_group_checked = 0
        childlist = []
        top_item_list = []
        model = self.sourceModel()
        if model is not None:
            for row in range(model.rowCount()):
                top_item = model.item(row)
                if top_item is not None:
                    if top_item.isCheckable() and top_item.checkState() == QtCore.Qt.Checked:
                        if not top_item.hasChildren() and (not top_item in top_item_list):
                            total_name_checked += 1
                            top_item_list.append(top_item.text())
                        if top_item.hasChildren() and (not top_item in top_item_list):
                            total_group_checked += 1
                            top_item_list.append(top_item.text())
                    top_item_total_name_checked, top_item_total_group_checked = count_checked_recursive(top_item)
                    total_name_checked += top_item_total_name_checked
                    total_group_checked += top_item_total_group_checked

        return total_name_checked, total_group_checked