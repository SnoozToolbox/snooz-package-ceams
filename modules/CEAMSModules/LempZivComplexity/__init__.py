"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
from .LempZivComplexity import LempZivComplexity
from .LempZivComplexitySettingsView import LempZivComplexitySettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .LempZivComplexityResultsView import LempZivComplexityResultsView
    from .Ui_LempZivComplexityResultsView import Ui_LempZivComplexityResultsView
    from .Ui_LempZivComplexitySettingsView import Ui_LempZivComplexitySettingsView
else:
    # Create stub classes for headless mode
    LempZivComplexityResultsView = None
    Ui_LempZivComplexityResultsView = None
    Ui_LempZivComplexitySettingsView = None