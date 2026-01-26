"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
from .RandB import RandB
from .RandBSettingsView import RandBSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
     from .RandBResultsView import RandBResultsView
     from .Ui_RandBResultsView import Ui_RandBResultsView
     from .Ui_RandBSettingsView import Ui_RandBSettingsView
else:
    # Create stub classes for headless mode
    RandBResultsView = None
    Ui_RandBResultsView = None
    Ui_RandBSettingsView = None