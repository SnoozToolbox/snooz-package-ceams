"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PSACompilation import PSACompilation
from .PSACompilationSettingsView import PSACompilationSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
try:
    import config
    if not config.HEADLESS_MODE:
        from .PSACompilationResultsView import PSACompilationResultsView
        from .Ui_PSACompilationResultsView import Ui_PSACompilationResultsView
        from .Ui_PSACompilationSettingsView import Ui_PSACompilationSettingsView
    else:
        # Create stub classes for headless mode
        PSACompilationResultsView = None
        Ui_PSACompilationResultsView = None
        Ui_PSACompilationSettingsView = None
except (ImportError, AttributeError):
    # If config is not available, import normally (for backward compatibility)
    from .PSACompilationResultsView import PSACompilationResultsView
    from .Ui_PSACompilationResultsView import Ui_PSACompilationResultsView
    from .Ui_PSACompilationSettingsView import Ui_PSACompilationSettingsView