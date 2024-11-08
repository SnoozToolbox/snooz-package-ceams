"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem, QGraphicsObject
from qtpy.QtCore import QRectF, Qt, Slot, Signal, QObject
from qtpy.QtGui import QPainter, QColor

from CEAMSApps.EEGViewer.widgets.SignalsWidget.EventNameItem import EventNameItem

class ScaleButtonObject(QGraphicsObject):
    on_pressed = Signal()

    def __init__(self, width, height, isplus):
        super().__init__()
        self._rect = QRectF(0,0,width,height)
        self._isplus = isplus
        
    ## UI EVENTS
    def boundingRect(self):
        return self._rect
    
    def paint(self, painter: QPainter, option, widget):
        painter.setPen(Qt.black)
        painter.drawRect(self.boundingRect())

        # Draw plus and minus signs
        pen = painter.pen()
        pen.setColor(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        padding = 3
        if self._isplus:
            painter.drawLine(self._rect.left() + padding, self._rect.height()/2, self._rect.right() - padding, self._rect.height()/2)
            painter.drawLine(self._rect.left() + self._rect.width()/2, self._rect.top() + padding, self._rect.left() + self._rect.width()/2, self._rect.bottom() - padding)
        else:
            painter.drawLine(self._rect.left() + padding, self._rect.height()/2, self._rect.right() - padding, self._rect.height()/2)            
        

    def mousePressEvent(self, event):
        self.on_pressed.emit()

class ScaleItem(QGraphicsItem):

    def __init__(self, signal_model, width):
        super().__init__()
        self._signal_model = signal_model
        self._bg_brush = QColor(255,0,255,30)
        self._width = width
        self._fourth = self._width / 4
        y_padding = 1
        
        self._signal_model.data_changed.connect(self.on_data_changed)

        self._scaleDownButton = ScaleButtonObject(self._fourth,self._fourth, False)
        self._scaleDownButton.setPos(5,y_padding)
        self._scaleDownButton.setParentItem(self)
        self._scaleDownButton.on_pressed.connect(self.on_scale_down)

        self._scaleUpButton = ScaleButtonObject(self._fourth,self._fourth, True)
        self._scaleUpButton.setPos(self._fourth * 3 - 5,y_padding)
        self._scaleUpButton.setParentItem(self)
        self._scaleUpButton.on_pressed.connect(self.on_scale_up)
        

    # After init thgis function is called

    ## PROPERTIES
    
    ## SLOTS
    Slot()
    def on_data_changed(self):
        # Repaint
        self.update()

    Slot()
    def on_scale_up(self):
        self._signal_model.amp_scale += 0.2

    Slot()
    def on_scale_down(self):
        self._signal_model.amp_scale = max(0, self._signal_model.amp_scale - 0.2)

    ## UI EVENTS
    def boundingRect(self):
        return QRectF(0,0,self._width,self._width/3)
    
    def paint(self, painter: QPainter, option, widget):
        pass