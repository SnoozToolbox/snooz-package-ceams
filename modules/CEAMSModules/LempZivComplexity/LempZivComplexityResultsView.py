"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Results viewer of the LempZivComplexity plugin
"""

from qtpy import QtWidgets
from qtpy.QtCore import Qt

from CEAMSModules.LempZivComplexity.Ui_LempZivComplexityResultsView import (
    Ui_LempZivComplexityResultsView,
)


class LempZivComplexityResultsView(Ui_LempZivComplexityResultsView, QtWidgets.QWidget):
    """Show a short summary written to mem-cache by LempZivComplexity.compute()."""

    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(LempZivComplexityResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager
        self.setupUi(self)

        # Scaffold .ui has an empty layout; add a label for the cache summary.
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setWordWrap(True)
        self.result_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        if hasattr(self, 'result_layout'):
            self.result_layout.addWidget(self.result_label)
        else:
            self.verticalLayout.addWidget(self.result_label)

    def load_results(self):
        cache = None
        try:
            cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        except Exception:
            cache = None

        if not cache:
            self.result_label.setText(
                'No LZC results in cache yet. Run the process first.'
            )
            return

        lines = [
            f"mode: {cache.get('mode')}",
            f"epochs kept / rejected: "
            f"{cache.get('n_epochs_kept')} / {cache.get('n_epochs_rejected')}",
            f"average_lzc: {cache.get('average_lzc')}",
            f"per_epoch mean ± std: "
            f"{cache.get('per_epoch_lzc_mean')} ± {cache.get('per_epoch_lzc_std')}",
            f"n channels: {len(cache.get('channel_names') or [])}",
        ]
        if cache.get('warning'):
            lines.append(str(cache.get('warning')))
        if cache.get('cohort_filename'):
            lines.append(f"cohort report: {cache.get('cohort_filename')}")
        export_files = cache.get('export_files') or []
        if export_files:
            lines.append(f"{len(export_files)} file(s) written, first: {export_files[0]}")
        avg_ch = cache.get('average_per_channel_lzc')
        if avg_ch is not None:
            names = cache.get('channel_names') or []
            preview = ', '.join(
                f"{names[i] if i < len(names) else i}={avg_ch[i]:.4f}"
                for i in range(min(8, len(avg_ch)))
            )
            if len(avg_ch) > 8:
                preview += ', ...'
            lines.append(f"average_per_channel (first): {preview}")

        self.result_label.setText('\n'.join(lines))
