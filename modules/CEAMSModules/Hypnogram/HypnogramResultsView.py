"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the Hypnogram plugin

    A hypnogram is a form of polysomnography; it is a graph that represents the 
    stages of sleep as a function of time.

    Takes sleep stages and sleep cycles in parameter. A sleep cycle is 
    defined as a period of NREM sleep followed by a period of REM sleep.

"""
from ..PSGReader import commons

import matplotlib
from numpy import ceil
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import math
import numpy as np

from qtpy import QtWidgets

from CEAMSModules.Hypnogram.Ui_HypnogramResultsView import Ui_HypnogramResultsView

class HypnogramResultsView( Ui_HypnogramResultsView, QtWidgets.QWidget):
    """
        HypnogramResultsView displays an hypnogram based on the stages in input
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(HypnogramResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self) 

        self.figure = Figure(constrained_layout=False)
        self.hypno_ax = self.figure.add_subplot(111)
        self.hypno_ax.clear()

        # Add the figure tool bar
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(self.canvas)


    def load_results(self):
        self.cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if self.cache is not None:
            sleep_stages = self.cache['sleep_stages']
            epoch_len = self.cache['epoch_len_sec']
            sleep_cycles = self.cache['sleep_cycles']

            # Plot Hypnogram
            if sleep_stages is not None:
                self.plot_hypnogram(sleep_stages, sleep_cycles, epoch_len=epoch_len)
            self.canvas.draw()
            
    
    #def plot_hypnogram(self, hypno_ax, sleep_stages, sleep_cycles, epoch_len=None):
    def plot_hypnogram(self, sleep_stages, sleep_cycles, epoch_len=None):
        """ Plot an hypnogram based on the sleep stages in parameter 
        
        Parameters
        ----------
            sleep_stages : Panda dataframe
                List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
            epoch_len : integer (optional)
                Length of the epoch in seconds

        Returns
        -----------
            None
        """

        hypno_y_label = ["Unscored", "N3","N2","N1","R","Wake", "Cycles"]

        # Combined configuration for sleep stages: plot position and color
        stage_config = {
            "0": {"plot_pos": 5, "color": "white"},         # Awake
            "5": {"plot_pos": 4, "color": "green"},         # REM
            "1": {"plot_pos": 3, "color": "cornflowerblue"}, # N1
            "2": {"plot_pos": 2, "color": "blue"},          # N2
            "3": {"plot_pos": 1, "color": "darkblue"},      # N3
            "9": {"plot_pos": 0, "color": "gray"},          # Unscored
            "8": {"plot_pos": 0, "color": "gray"},          # etc.
            "7": {"plot_pos": 0, "color": "gray"},
        }

        # Derive level colors from stage config
        level_colors = {}
        for stage, config in stage_config.items():
            level_colors[config["plot_pos"]] = config["color"]

        # Hypnogram color definition for sleep cycles
        #                           R           G       B
        fill_color_complete_NREM =  [0/255, 32/255, 128/255]    # Colors values are between 0 and 1
        fill_color_complete_REM =   [0/255, 64/255, 0/255]      # Colors values are between 0 and 1
        fill_color_incomplete =     [150/255, 0/255, 0/255]     # Colors values are between 0 and 1
        alpha = 0.3

        # Remove unscored stages at the beginning and the end
        stages = []
        sleep_stages_nocycle = sleep_stages[sleep_stages.group == commons.sleep_stages_group].copy()
        sleep_stages_nocycle.reset_index(inplace=True, drop=True)
        sleep_stages_nocycle.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')
        scoring_start = sleep_stages_nocycle[(sleep_stages_nocycle['name']!='9') & (sleep_stages_nocycle['name']!='8')].first_valid_index()
        scoring_end = sleep_stages_nocycle[(sleep_stages_nocycle['name']!='9') & (sleep_stages_nocycle['name']!='8')].last_valid_index()
        all_stages = sleep_stages_nocycle['name'].values.tolist()
        if (not scoring_start==None) and (not scoring_end==None):
            scored_stages = all_stages[scoring_start:scoring_end+1]
        else:
            scored_stages = all_stages

        # Convert all stages to they plot value
        for s in scored_stages:
            stage = stage_config.get(s, {"plot_pos": 0})["plot_pos"]
            stages.append(stage)
        
        # Create color list based on original stage values
        colors = [stage_config.get(s, {"color": 'blue'})["color"] for s in scored_stages]
        
        # Draw background rectangles for each level (corresponding to sleep stages)
        for level in range(6): # From the number of unique values to plot (the 7 levels for stages)
            self.hypno_ax.add_patch(Rectangle((0, level - 0.5), len(stages), 1,
                facecolor=level_colors[level], alpha=alpha, edgecolor='none'))

        # Plot the hypnogram contour (black line)
        self.hypno_ax.plot(range(len(stages)), stages, color='black', linewidth=1)
        #self.hypno_ax.bar(range(len(stages)),stages, width=1,align='edge')
        self.hypno_ax.set_yticks(range(len(hypno_y_label)))
        self.hypno_ax.set_yticklabels([])
        self.hypno_ax.set_yticklabels(hypno_y_label)
        self.hypno_ax.set_ylabel('Sleep Stage')
        self.hypno_ax.set_xlabel('Elapsed Time (epoch)')
        # If the epoch length is defined, change the x axis for hour instead of epoch
        if isinstance(epoch_len, int) or isinstance(epoch_len, float):
            max_sec = len(scored_stages) * epoch_len
            max_hour = math.ceil(max_sec/3600)
            self.hypno_ax.set_xticks(np.arange(max_hour)*3600/epoch_len)
            lst_hour = range(max_hour)
            xticklabels=["{:02d}".format(x) for x in lst_hour]
            self.hypno_ax.set_xticklabels([])
            self.hypno_ax.set_xticklabels(xticklabels)
            self.hypno_ax.set_xlabel('Elapsed Time (h)')
            # Path to generate the picture
            #self.hypno_ax.set_title(f'Hypnogram with Sleep Cycles')
            self.hypno_ax.set_title(f'Hypnogram with Sleep Cycles - {self.subject_id}')

        if sleep_cycles is not None:
            HypnogramResultsView.draw_sleep_cycles(self, sleep_cycles, scoring_start, 
                fill_color_complete_NREM, fill_color_complete_REM, fill_color_incomplete, alpha)
            
            # Add legend for sleep cycle patches
            legend_patches = [
                Rectangle((0, 0), 1, 1, facecolor='black', label='Sleep Stages'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_complete_NREM, alpha=alpha, label='NREM Period'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_complete_REM, alpha=alpha, label='REM Period'),
                Rectangle((0, 0), 1, 1, facecolor=fill_color_incomplete, alpha=alpha, label='Incompl. Period')
            ]
            self.hypno_ax.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8, framealpha=0.9)


    #def draw_sleep_cycles(self, hypno_ax, sleep_cycles, scoring_start):
    def draw_sleep_cycles(self, sleep_cycles, scoring_start, 
        fill_color_complete_NREM, fill_color_complete_REM, fill_color_incomplete, alpha):
        """ Draw sleep cycles over the hypnogram.
        A sleep cycle is compose of two period, the NREM and REM period. The NREM period is identified
        by a rectangle that cover the stages 1,2,3 and the REM period is identified by a rectangle that
        cover the REM stage.
        
        Parameters
        ----------
            sleep_cycles : List of tuples
                Each element of the list defines a sleep cycle. The first tuple is the 
                beginning and end of the NREM period. The second tuple is the beginning 
                and end of the REM period. Both beginning and end are inclusive indexes.
                The last variable [is_complete] tells of this cycle is complete. An incomplete
                cycle would be one without a REM period, it's often found at the end of the night.
                ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)

        Returns
        -----------
            None
        """
        # Plot the sleep cycles
        for index, (nrem, rem, is_complete) in enumerate(sleep_cycles):

            # NREM
            width = nrem[1] - nrem[0] +1  # the bounderies are inclusive
            if width >= 0:
                self.hypno_ax.add_patch(Rectangle((nrem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                facecolor = fill_color_complete_NREM if is_complete else fill_color_incomplete,
                alpha = alpha,
                edgecolor = 'black',
                fill=True,
                linewidth=0.5))

                # Draw a black outline
                self.hypno_ax.add_patch(Rectangle((nrem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                edgecolor = 'black',
                fill=False,
                linewidth=0.5))

            # REM
            width = rem[1] - rem[0] +1 # the bounderies are inclusive 
            if width >= 0:
                self.hypno_ax.add_patch(Rectangle((rem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                facecolor = fill_color_complete_REM if is_complete else fill_color_incomplete,
                alpha = alpha,
                edgecolor = 'black',
                fill=True,
                linewidth=0.5))

                # Draw a black outline
                self.hypno_ax.add_patch(Rectangle((rem[0]-scoring_start, 5.2), width, 6,
                linestyle = '-' if is_complete else '--',
                edgecolor = 'black',
                fill=False,
                linewidth=0.5))

        # Draw horizontal arrows for complete sleep cycles
        for index, (nrem, rem, is_complete) in enumerate(sleep_cycles):
            if is_complete:
                # Calculate the full cycle span (from NREM start to REM end)
                cycle_start = min(nrem[0], rem[0]) - scoring_start
                cycle_end = max(nrem[1], rem[1]) - scoring_start
                cycle_width = cycle_end - cycle_start
                
                # Draw horizontal arrow at Wake level (y=5)
                # Arrow from cycle_start to cycle_end, centered vertically at y=5
                arrow_y = 5.6
                arrow_length = cycle_width
                
                # Use annotate for better arrow control
                self.hypno_ax.annotate('',
                    xy=(cycle_end, arrow_y),  # Arrow head position
                    xytext=(cycle_start, arrow_y),  # Arrow tail position
                    arrowprops=dict(
                        arrowstyle='<->',  # Double-headed arrow
                        color='black',
                        linewidth=1,
                        shrinkA=0,
                        shrinkB=0
                    ),
                    annotation_clip=False
                )
                
                # Add cycle label (C1, C2, etc.) above the arrow
                cycle_center_x = (cycle_start + cycle_end) / 2
                cycle_label = f'C{index + 1}'
                self.hypno_ax.text(cycle_center_x, arrow_y, cycle_label,
                    ha='center', va='center', fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
