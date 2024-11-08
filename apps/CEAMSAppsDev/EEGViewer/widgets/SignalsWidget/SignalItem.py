"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem, QLabel
from qtpy.QtCore import QRectF, Slot, Qt
from qtpy.QtGui import QPainter, QPainterPath

#from managers.PubSubManager import PubSubManager
from CEAMSApps.EEGViewer.widgets.SignalsWidget.EventItem import EventItem
from CEAMSApps.EEGViewer.widgets.SignalsWidget.ScaleItem import ScaleItem

class SignalItem(QGraphicsItem):
    # Signal on data change
    def __init__(self, signal_model):
        super().__init__()
        self.setZValue(1)
        self._signal_path = QPainterPath()
        self._grid_color = Qt.lightGray
        self._signal_pen_color = Qt.blue
        self._display_width = 400
        self._left_padding = 50
        self._min = -20
        self._max = 20
        self._old_min = 0
        self._old_max = 0
        
        self._signal_model = signal_model
        self._signal_model.data_changed.connect(self.on_data_changed)

        for event_model in self._signal_model.event_models:
            event_item = EventItem(event_model)
            event_item.setParentItem(self)

        self.scale_item = ScaleItem(self._signal_model, self._left_padding)
        self.scale_item.setParentItem(self)

    @property
    def signal_window_width(self):
        return self._display_width - self._left_padding
    
    Slot()
    def on_data_changed(self):
        self._update_signal_path()
        self.update()

    @Slot()
    def on_drawing_parameters_changed(self, parameters):
        """
        Update the drawing parameters and adjust the position of child EventItems accordingly.

        Parameters:
            parameters (DrawingParameters): The new drawing parameters.

        Returns:
            None
        """
        #self._drawing_parameters = parameters
        self._display_width = parameters.display_width
        self._time_offset = parameters.time_offset
        self._seconds_per_page = parameters.seconds_per_page
        for item in self.childItems():
            if isinstance(item, EventItem):
                # Update the position
                x = (item.start_time - parameters.time_offset) * \
                    parameters.pixel_per_second + self._left_padding

                item.setPos(x, item.pos().y())

                # Call the item to update itself
                item.on_drawing_parameters_changed(parameters)

        self._update_signal_path()
        self.update()

    ## UI EVENTS
    def boundingRect(self):
        w = self._display_width - 5
        h = self._max - self._min
        x = 0
        y = self._min
        return QRectF(x,y,w,h)
    
    def paint(self, painter: QPainter, option, widget):
        def _set_font_size(size):
            font = painter.font()
            font.setPointSize(size)
            painter.setFont(font)
        def _set_font_bold(is_bold):
            font = painter.font()
            font.setBold(is_bold)
            painter.setFont(font)

        # paint zero line
        painter.setPen(self._grid_color)
        painter.drawLine(self._left_padding, 0,self._display_width,0)

        #Paint signal
        pen = painter.pen()
        pen.setWidthF(0.5)
        pen.setColor(self._signal_pen_color)
        painter.setPen(pen)
        painter.drawPath(self._signal_path)

        # Draw the channel name
        _set_font_size(10)
        _set_font_bold(True)
        painter.setPen(Qt.black)
        painter.drawText(5,-4,f"{self._signal_model.channel_name}")

    def _update_signal_path(self):
        self._signal_path.clear()
        self._first_index = int(self._time_offset * self._signal_model.sample_rate)

        # Calculate how much samples there is to draw based on the time cursor
        # and the total signal size
        samples_to_draw = int(self._seconds_per_page * self._signal_model.sample_rate)
        
        if samples_to_draw > 0:
            # x_ratio is the space in pixel between samples (can be a float value)
            self._x_ratio = self.signal_window_width / samples_to_draw

            #Adjust the amout to draw based on how many there is left to draw
            self._samples_to_draw = int(min(samples_to_draw, self._signal_model.get_total_sample_count() - self._first_index))

            # Draw the signal
            is_last_none = False
            if self._samples_to_draw > 0:
                
                y = self._signal_model.get_sample_by_index(self._first_index)
                if y is None:
                    y = 0
                self._signal_path.moveTo(self._left_padding, y*self._signal_model.amp_scale)
                self._min = 0
                self._max = 0
                for i in range(self._samples_to_draw):
                    x = i * self._x_ratio + self._left_padding
                    y = self._signal_model.get_sample_by_index(self._first_index + i)
                    if y is None:
                        y = 0
                        self._signal_path.moveTo(x, y*self._signal_model.amp_scale)
                        is_last_none = True
                    elif is_last_none:
                        self._signal_path.moveTo(x, y*self._signal_model.amp_scale)
                        is_last_none = False
                    else:
                        self._signal_path.lineTo(x, y*self._signal_model.amp_scale)

                    self._min = min(self._min, y*self._signal_model.amp_scale)
                    self._max = max(self._max, y*self._signal_model.amp_scale)
                    
                if self._old_min != self._min or self._old_max != self._max:
                    self.prepareGeometryChange()
                    self._old_min = self._min
                    self._old_max = self._max

    