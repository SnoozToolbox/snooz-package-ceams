"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the AliasSignals plugin
"""


# Conditionally import matplotlib based on headless mode
try:
    import config
    if config.HEADLESS_MODE:
        # Use Agg backend in headless mode (no GUI required, perfect for PDF generation)
        import matplotlib
        matplotlib.use('Agg')
        from matplotlib.figure import Figure
        import matplotlib.pyplot as plt
    else:
        # Use QtAgg backend in GUI mode
        import matplotlib
        matplotlib.use('QtAgg')
        from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
        from matplotlib.figure import Figure
        import matplotlib.pyplot as plt
    # If config is not available, default to QtAgg (for backward compatibility)

import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.AliasSignals.Ui_AliasSignalsResultsView import Ui_AliasSignalsResultsView

class AliasSignalsResultsView( Ui_AliasSignalsResultsView, QtWidgets.QWidget):
    """
        AliasSignalsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(AliasSignalsResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        pass
        