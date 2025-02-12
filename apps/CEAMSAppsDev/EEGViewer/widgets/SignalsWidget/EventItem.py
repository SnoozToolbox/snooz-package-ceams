"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem
from qtpy.QtCore import QRectF, Qt, Slot
from qtpy.QtGui import QPainter, QColor

from CEAMSApps.EEGViewer.widgets.SignalsWidget.EventNameItem import EventNameItem

class EventItem(QGraphicsItem):

    def __init__(self, event_model):
        super().__init__()
        self._event_model = event_model
        self._pixel_per_second = 0
        self._signal_row_height = 0
        self._bg_brush = QColor(255,0,0,30)
        self._is_hovering = False
        self.setAcceptHoverEvents(True)
        self.setZValue(4)
        self._event_model.data_changed.connect(self.on_data_changed)

        self._name_item = EventNameItem(self._event_model.group, self._event_model.name)
        self._name_item.setParentItem(self)

    ## PROPERTIES
    @property
    def start_time(self):
        return self._event_model.start_sec
    
    Slot()
    def on_data_changed(self):
        self.update()

    ## UI EVENTS
    def boundingRect(self):
        return self._event_rect()
    
    def paint(self, painter: QPainter, option, widget):
        painter.setPen(Qt.red)
        painter.setBrush(self._bg_brush)
        painter.drawRect(self._event_rect())

        self._name_item.setVisible(self._is_hovering)

    def hoverEnterEvent(self, event):
        self._is_hovering = True
        self.update()

    def hoverLeaveEvent(self, event):
        self._is_hovering = False
        self.update()
    
    # Public functions
    def on_drawing_parameters_changed(self, drawing_parameters):
        self._pixel_per_second = drawing_parameters.pixel_per_second
        self._signal_row_height = drawing_parameters.signal_row_height

        self._name_item.setPos(self._name_item.pos().x(), self._signal_row_height/2)
        self.prepareGeometryChange()
        self.update()

    def _event_rect(self):
        w = self._pixel_per_second * self._event_model.duration_sec
        h = self._signal_row_height
        x = 0
        y = -(self._signal_row_height / 2)
        return QRectF(x,y,w,h)