"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .RnB import RnB
from .RnBSettingsView import RnBSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .RnBResultsView import RnBResultsView
    from .Ui_RnBResultsView import Ui_RnBResultsView
    from .Ui_RnBSettingsView import Ui_RnBSettingsView
else:
    # Create stub classes for headless mode
    RnBResultsView = None
    Ui_RnBResultsView = None
    Ui_RnBSettingsView = None