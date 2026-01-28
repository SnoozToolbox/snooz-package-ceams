"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    Results viewer of the RandB plugin
"""

from qtpy import QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.Stft.plot_helper import draw_spectogram
from CEAMSModules.Stft.Ui_StftResultsView import Ui_StftResultsView


from CEAMSModules.RandB.Ui_RandBResultsView import Ui_RandBResultsView

class RandBResultsView(Ui_RandBResultsView, QtWidgets.QWidget):
    """
        RandBResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(RandBResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # To manage the disk cache to navigate through epochs
        self.filename = []
        self.disk_cache = {}

        # To manage the figure on the layout result_layout
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)
        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)        

    def load_results(self):
        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:
            # Get the data needed in the spectogram
            win_len = cache['win_len']
            win_step = cache['win_step_sec']
            psd = cache['psd']
            freq_bins = cache['freq_bins']
            first_freq = cache['first_freq']
            last_freq = cache['last_freq']
            psd_raw = cache['psd_raw']
            freq_raw = cache['freq_raw']

    #            self.filename = cache['filename']
                # Call the display function
            self._plot_resultsView(psd, win_len, win_step, 0, psd.shape[0], freq_bins,first_freq, last_freq, psd_raw,freq_raw)
        else:
            self.figure.clear() # reset the hold on 
            # Redraw the figure, needed when the show button is pressed more than once
            self.canvas.draw()     


    def _plot_resultsView(self, psd, win_len, win_step_sec, winshow_start_win, \
        winshow_len_win, freq_bins, first_freq, last_freq, psd_raw,freq_raw):
        
        #-----------------
        # Manage figure
        #-----------------
        self.figure.clear() 
        # first subplot
        ax1 = self.figure.add_subplot(121)
        ax1.set_xscale('log')
        ax1.set_yscale('log')
        ax1.set(xticklabels=[])
        # ommit first frequency in case it starts at 0hz
        ax1.plot(freq_raw[1:],psd_raw[1:], color = 'blue'); 
        ax1.axvline(x=(freq_bins[1]), color='red', linestyle='--') 
        ax1.axvline(x=(last_freq), color='red', linestyle='--') 
        xtick_locs = [1, 2, 4, 8, 16, 32, 64 ,128] 
        xtick_labels = ['1', '2', '4', '8', '16', '32', '64' , '128'] 
        ax1.set_xticks(xtick_locs)
        ax1.set_xticklabels(xtick_labels)
        ax1.set_xlabel('Frequency (Hz)') 
        ax1.set_ylabel('Power') 
        ax1.set_title('Average spectrum') 
        # first subplot
        ax2 = self.figure.add_subplot(122)
        ax2.set_xscale('log')
        ax2.set(xticklabels=[])
        ax2.plot(freq_bins,psd , color = 'blue'); 
        ax2.axhline((1), color='black', linestyle='--')
        xtick_locs = [1, 2, 4, 8, 16, 32, 64 ,128] 
        xtick_labels = ['1', '2', '4', '8', '16', '32', '64' , '128'] 
        ax2.set_xticks(xtick_locs)
        ax2.set_xticklabels(xtick_labels)
        ax2.set_xlabel('Frequency (Hz)') 
        ax2.set_ylabel('Power') 
        ax2.set_title('Rythmic spectrum') 

        # refresh canvas
        self.figure.tight_layout()
        self.canvas.draw()