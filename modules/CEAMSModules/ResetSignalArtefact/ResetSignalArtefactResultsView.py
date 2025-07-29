# """
# @ Valorisation Recherche HSCM, Societe en Commandite – 2023
# See the file LICENCE for full license details.
# """

# """
#     Results viewer of the ResetSignalArtefact plugin
# """

# # Take the the result view from the CsvReader
# # CsvReader results view show a dataframe of events
# from CEAMSModules.EventReader.EventReaderResultsView import EventReaderResultsView

# class ResetSignalArtefactResultsView(EventReaderResultsView):
#     """
#         ResetSignalArtefactResultsView shows selected artefact event
#     """
#     pass


from qtpy import QtWidgets
import pandas as pd

class ResetSignalArtefactResultsView(QtWidgets.QWidget):
    """
    Show which artefact windows were reset (zero-ed or NaN-ed)
    and on which channels.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node   = parent_node
        self._cache_manager = cache_manager

        layout = QtWidgets.QVBoxLayout(self)

        self.ch_label = QtWidgets.QLabel("Channels modified:")
        self.ch_text  = QtWidgets.QPlainTextEdit()
        self.ch_text.setReadOnly(True)

        self.ev_label = QtWidgets.QLabel("Artefact windows reset:")
        self.ev_table = QtWidgets.QTableWidget()
        self.ev_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        layout.addWidget(self.ch_label)
        layout.addWidget(self.ch_text)
        layout.addWidget(self.ev_label)
        layout.addWidget(self.ev_table)
        self.setLayout(layout)

        # immediately fill from whatever is in cache
        self.load_results()

    def load_results(self):
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier) or {}

        # 1) Channels modified
        masked = cache.get('masked_channels', [])
        self.ch_text.setPlainText("\n".join(masked) if masked else "(none)")

        # 2) Events you actually selected
        df = cache.get('events', pd.DataFrame())
        if not df.empty:
            self.ev_table.setColumnCount(len(df.columns))
            self.ev_table.setRowCount(len(df))
            self.ev_table.setHorizontalHeaderLabels(df.columns.tolist())
            for r in range(len(df)):
                for c, col in enumerate(df.columns):
                    val = df.iloc[r, c]
                    item = QtWidgets.QTableWidgetItem(str(val))
                    self.ev_table.setItem(r, c, item)
            self.ev_table.resizeColumnsToContents()
        else:
            self.ev_table.clear()
            self.ev_table.setRowCount(0)
            self.ev_table.setColumnCount(0)



