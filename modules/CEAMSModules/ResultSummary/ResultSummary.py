"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    ResultSummary
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd
import os

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np

DEBUG = False

class ResultSummary(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        ResultsDataframe: TODO TYPE
            TODO DESCRIPTION
        Additional: TODO TYPE
            TODO DESCRIPTION

    Returns
    -------
        ExportResults: TODO TYPE
            TODO DESCRIPTION
    """
    def __init__(self, **kwargs):
        """ Initialize module ResultSummary """
        super().__init__(**kwargs)
        if DEBUG: print('ResultSummary.__init__')

        # Input plugs
        InputPlug('ResultsDataframe', self)
        InputPlug('Additional', self)
        InputPlug('SavedDestination', self)
        InputPlug('Checkbox', self)

        # Output plugs
        OutputPlug('ExportResults', self)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        # A master module allows the process to be reexcuted multiple times.
        # For example, this is useful when the process must be repeated over multiple
        # files. When the master module is done, i.e., when all the files were processed,
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False
        self.AccuracyList = []

    def compute(self, ResultsDataframe, Additional, SavedDestination, Checkbox):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            ResultsDataframe: TODO TYPE
                TODO DESCRIPTION
            Additional: TODO TYPE
                TODO DESCRIPTION

        Returns
        -------
            ExportResults: TODO TYPE
                TODO DESCRIPTION

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if Checkbox:
            # Define file path
            export_results_file_path = '../snooz-package-ceams/modules/CEAMSModules/ResultSummary/ExportResults.xlsx' # You need to change this path to your own path

            # Check if file exists, if not create it with headers
            if not os.path.exists(export_results_file_path):
                pd.DataFrame().to_excel(export_results_file_path, index=False)

            # Load existing data
            try:
                export_results_df = pd.read_excel(export_results_file_path)
            except pd.errors.EmptyDataError:
                export_results_df = pd.DataFrame()

            # Append new data
            export_results_df = pd.concat([export_results_df, ResultsDataframe], ignore_index=True)

            # Save updated data back to excel file
            export_results_df.to_excel(export_results_file_path, index=False)

            # Plot the hypnogram and confusion matrix and save to a PDF file
            self.figure.clear() # reset the hold on
            self.figure.set_size_inches(15,4)
            ### Plot the hypnogram
            # Define the layout for the plots
            gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])  # Three equal-height plots
            
            #confidence = cache['y_pred_new'].proba.max(axis=1)
            #print(confidence)
            # Adjust the layout to make each subplot bigger
            gs.update(wspace=0.4, hspace=0.6)
            # First subplot - Hypnogram
            labels_new = Additional[0]
            ax1 = self.figure.add_subplot(gs[0])
            ax1 = labels_new.plot_hypnogram(fill_color="gainsboro", ax=ax1)
            ax1.set_title('Expert Annotated Hypnogram')
            ax1.set_xlabel('Time (h)')
            ax1.set_ylabel('Sleep stage')
            ax1.grid()

            # Second subplot - Estimated Hypnogram
            y_pred_new = Additional[1]
            ax2 = self.figure.add_subplot(gs[2])
            ax2 = y_pred_new.plot_hypnogram(fill_color="blue", ax=ax2)
            ax2.set_title('Estimated Hypnogram')
            ax2.set_xlabel('Time (h)')
            ax2.set_ylabel('Sleep stage')
            ax2.grid()

            # Compute confusion matrix
            y_true = labels_new.hypno.values
            y_pred = y_pred_new.hypno.values
            class_labels = ['WAKE', 'N1', 'N2', 'N3', 'REM']
            cm = confusion_matrix(y_true, y_pred, labels=class_labels)
            cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
            
            # Set the labels for the confusion matrix
            tick_marks = np.arange(len(class_labels))
            # Third subplot - Confusion Matrix
            ax3 = self.figure.add_subplot(gs[1])
            sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', ax=ax3)
            ax3.set_title('Confusion Matrix')
            ax3.set_xlabel('Predicted')
            ax3.set_ylabel('True')
            ax3.set_xticks(tick_marks)
            ax3.set_xticklabels(class_labels)
            ax3.set_yticks(tick_marks)
            ax3.set_yticklabels(class_labels)
            # Fourth subplot - Accuracy and Average Confidence
            ax4 = self.figure.add_subplot(gs[3])
            ax4.axis('off')
            # Add accuracy and average confidence text next to the subplots
            ax4.text(0.5, 0.5, f"Accuracy: {ResultsDataframe['Accuracy'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
            ax4.text(0.5, 0.3, f"Avg Confidence: {ResultsDataframe['Average Confidence'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
            
                                # Adjust layout to add more space between subplots
            self.figure.tight_layout(pad=10.0)

                    # Save the figure to a PDF file
            filename = os.path.basename(Additional[2])
            name_without_extension = os.path.splitext(filename)[0]
            file_name = SavedDestination + name_without_extension
            if isinstance(file_name, str) and (len(file_name)>0):
                if not '.' in file_name:
                    file_name = file_name + '.pdf'
            self.figure.savefig(file_name, format='pdf')

            # refresh canvas
            self.canvas.draw()
            # Return the path to the updated Excel file
        else:
            export_results_file_path = None

        return {
            'ExportResults': export_results_file_path
        }
