"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QWidget, QPushButton,QGraphicsItem, QComboBox, QLabel, QGraphicsScene, QVBoxLayout, QGraphicsView, QScrollBar, QHBoxLayout
from qtpy.QtCore import Qt, Signal, Slot
from qtpy.QtGui import QPainter

from CEAMSApps.EEGViewer.widgets.SignalsWidget.SignalItem import SignalItem
from CEAMSApps.EEGViewer.widgets.SignalsWidget.TimeMarkerItem import TimeMarkerItem
from CEAMSApps.EEGViewer.widgets.SignalsWidget.DrawingParameters import DrawingParameters

class RootItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

# Subclass QMainWindow to customize your application's main window
class SignalsWidget(QWidget):
    size_changed = Signal(int, int)

    def __init__(self, parent):
        super().__init__(parent)

        self._pub_sub_manager = None
        self._events_manager = None

        # Init variables
        self._dp = DrawingParameters()
        self._root_item = RootItem()
        self._root_item.setPos(0,0)
        self._signals_y_init_offset = 60
        self._signals_y_step_offset = 30
        self._signals_count = 0

        ## Setup UI
        root_layout = QVBoxLayout()

        # Set layout padding to zero
        root_layout.setContentsMargins(0,0,0,0)

        # setup buttons
        buttons_layout = QHBoxLayout()
        self._increase_amp_button = QPushButton("+")
        self._increase_amp_button.setMaximumWidth(20)
        self._decrease_amp_button = QPushButton("-")
        self._decrease_amp_button.setMaximumWidth(20)
        self._seconds_per_page_combo_box = QComboBox()
        self._seconds_per_page_combo_box.addItem("1", userData=1)
        self._seconds_per_page_combo_box.addItem("5", userData=5)
        self._seconds_per_page_combo_box.addItem("10", userData=10)
        self._seconds_per_page_combo_box.addItem("20", userData=20)
        self._seconds_per_page_combo_box.addItem("30", userData=30)
        self._seconds_per_page_combo_box.setCurrentText("30")
        self._seconds_per_page_combo_box.currentIndexChanged.connect(self._on_seconds_per_page_change)
        self._increase_amp_button.clicked.connect(self.on_increase_amplitude)
        self._decrease_amp_button.clicked.connect(self.on_decrease_amplitude)

        self._time_label = QLabel(f"  Time position: 0s")
        #self._time_label.setMinimumWidth(80)
        #self._time_label.setMaximumWidth(80)

        buttons_layout.addWidget(self._increase_amp_button)
        buttons_layout.addWidget(self._decrease_amp_button)
        buttons_layout.addWidget(self._seconds_per_page_combo_box)
        buttons_layout.addWidget(QLabel("Sec/Page"))
        buttons_layout.addWidget(self._time_label)
        
        buttons_layout.addStretch()
        root_layout.addLayout(buttons_layout)

        # setup scene
        scene_layout = QHBoxLayout()
        root_layout.addLayout(scene_layout)
        self._view = QGraphicsView()
        scene_layout.addWidget(self._view)
        self._channel_scrollbar = QScrollBar(Qt.Vertical)
        scene_layout.addWidget(self._channel_scrollbar)
        self._channel_scrollbar.valueChanged.connect(self._on_channel_scroll)

        self._scene = QGraphicsScene()
        self._view.setScene(self._scene)
        self._view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self._view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._view.setRenderHint(QPainter.Antialiasing)

        hscroll_layout = QHBoxLayout()
        self._time_offset_scrollbar = QScrollBar(Qt.Horizontal)
        hscroll_layout.addWidget(self._time_offset_scrollbar)
        root_layout.addLayout(hscroll_layout)
        self.setLayout(root_layout)


        ## Init the scene
        self._scene.addRect(0,0,1,1)
        rect = self._view.sceneRect()
        rect.setX(0)
        rect.setY(0)
        self._view.setSceneRect(rect)

        # Add seconds markers
        left_padding = 50
        step = (self._view.width() - left_padding) / self._dp.seconds_per_page
        for i in range(self._dp.seconds_per_page+1):
            time_marker = TimeMarkerItem()
            time_marker.setParentItem(self._root_item)
            time_marker.setData(0, i)
            x = left_padding + step * i
            time_marker.setPos(x, 0)
            self._scene.addItem(time_marker)

        # Init drawing parameters
        self._dp.display_width = self._view.width()
    
        self._time_offset_scrollbar.valueChanged.connect(self._on_time_offset_change)
        self._dp.drawing_parameters_changed.connect(self._on_drawing_parameters_changed)

    ## PROPERTIES
    @property
    def events_manager(self):
        return self._events_manager

    @events_manager.setter
    def events_manager(self, events_manager):
        self._events_manager = events_manager

    @property
    def pub_sub_manager(self):
        return self._pub_sub_manager

    @pub_sub_manager.setter
    def pub_sub_manager(self, pub_sub_manager):
        self._pub_sub_manager = pub_sub_manager

    ## SLOTS
    @Slot()
    def on_external_time_cursor_change(self, time_cursor):
        self._time_offset_scrollbar.valueChanged.disconnect(self._on_time_offset_change)
        self._time_offset_scrollbar.setValue(time_cursor)
        self._dp.time_offset = time_cursor
        self._time_offset_scrollbar.valueChanged.connect(self._on_time_offset_change)

    @Slot()
    def _on_drawing_parameters_changed(self, drawing_parameters:DrawingParameters):
        self._update_time_marker_positions(drawing_parameters.pixel_per_second)

    @Slot()
    def _on_time_offset_change(self, value):
        self._time_label.setText(f"  Time position: {value}s")
        self._dp.time_offset = value
        #self._pub_sub_manager.publish(self, "time_cursor_changed", value)

    @Slot()
    def _on_seconds_per_page_change(self, value):
        self._update_drawing_parameters()

    ## UI EVENTS
    def resizeEvent(self, event):
        # This method is called whenever the widget is resized
        self.size_changed.emit(self._view.width(), self._view.height())
        self._update_drawing_parameters()

    def wheelEvent(self, event) -> None:
        scroll_value = self._channel_scrollbar.value()
        if event.angleDelta().y() > 0:
            scroll_value -= 1
        elif event.angleDelta().y() < 0:
            scroll_value += 1
        else: return        
        self._channel_scrollbar.setValue(scroll_value)

    ## PUBLIC FUNCTIONS
    def on_events_changed(self, events):
        for item in self._scene.items():
            if isinstance(item, SignalItem):
                item.on_events_changed(events)

    def register_listeners(self):
        #self._pub_sub_manager.subscribe(self, "time_cursor_changed")
        self._increase_amp_button.clicked.connect(self._dp.on_increase_amplitude)
        self._decrease_amp_button.clicked.connect(self._dp.on_decrease_amplitude)

    def unregister_listeners(self):
        #self._pub_sub_manager.unsubscribe(self, "time_cursor_changed")
        self._increase_amp_button.clicked.disconnect(self._dp.on_increase_amplitude)
        self._decrease_amp_button.clicked.disconnect(self._dp.on_decrease_amplitude)

    def on_topic_update(self, topic, message, sender):
        if topic == "time_cursor_changed":
            self.on_external_time_cursor_change(message)

    def remove_all_signals(self):
        items_to_remove = []
        for item in self._scene.items():
            if isinstance(item, SignalItem):
                items_to_remove.append(item)
                
        for item in items_to_remove:
            self._scene.removeItem(item)

        self._signals_count = 0

    def create_signals_item(self, signal_models):
        for idx, signal_model in enumerate(signal_models):
            signal_item = SignalItem(signal_model)
            signal_item.setData(0, idx)
            self._dp.drawing_parameters_changed.connect(signal_item.on_drawing_parameters_changed)

            y = idx * 45 + 30
            signal_item.setPos(0, y)
            
            signal_item.setParentItem(self._root_item)
            self._scene.addItem(signal_item)

            # Update horizontal scrollbar maximum value
            maximum = max(self._time_offset_scrollbar.value(), signal_model.get_duration())
            self._time_offset_scrollbar.setMaximum(maximum)

        # Update vertical scrollbar maximum value
        self._channel_scrollbar.setMaximum(len(signal_models) - 1) # No sense to being able to scroll past the last one, so -1
        self._channel_scrollbar.setValue(0)
        self._view.viewport().update()

        # This will update all SignalItem and EventsItem with the proper drawing parameters
        self._dp.emit_changed_signal()

    def add_signal(self, signal_models):

        signal_item = SignalItem(signal_models, self._dp, self._pub_sub_manager)
        signal_item.setParentItem(self._root_item)
        signal_item.setData(0, self._signals_count)

        y = self._signals_count * self._dp.signal_row_height + self._signals_y_init_offset
        signal_item.setPos(0, y)
        self._scene.addItem(signal_item)
        self._signals_count = self._signals_count + 1
        
        # Update horizontal scrollbar maximum value
        maximum = max(self._time_offset_scrollbar.value(), signal_item.get_duration())
        self._time_offset_scrollbar.setMaximum(maximum)

        # Update vertical scrollbar maximum value
        self._channel_scrollbar.setMaximum(self._signals_count-1) # No sense to being able to scroll past the last one, so -1
        self._channel_scrollbar.setValue(0)
        self._view.viewport().update()
    
    ## PRIVATE FUNCTIONS
    def _update_drawing_parameters(self):
        self._dp.seconds_per_page = self._seconds_per_page_combo_box.currentData()
        self._dp.pixel_per_second = \
            (self._view.width() - self._dp.channels_sections_width) / \
            self._dp.seconds_per_page
        self._dp.display_width = self._view.width()
        self._dp.display_height = self._view.height()

    def _update_time_marker_positions(self, pixel_per_second):
        left_padding = 50
        step = pixel_per_second
        for item in self._scene.items():
            if isinstance(item, TimeMarkerItem):
                i = item.data(0)
                x = left_padding + step * i
                item.setPos(x, 0)
        self._view.viewport().update()

    def _on_channel_scroll(self, value):
        for item in self._scene.items():
            if isinstance(item, SignalItem):
                pos = item.pos()
                scroll_offset = value * self._dp.signal_row_height
                order = item.data(0)
                y = order * self._dp.signal_row_height + self._signals_y_init_offset - scroll_offset
                
                pos.setY(y)
                item.setPos(pos)

    @Slot()
    def on_increase_amplitude(self):
        for item in self._scene.items():
            if isinstance(item, SignalItem):
                item.scale_item.on_scale_up()
        

    @Slot()
    def on_decrease_amplitude(self):
        for item in self._scene.items():
            if isinstance(item, SignalItem):
                item.scale_item.on_scale_down()
        

    