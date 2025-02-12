"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem
from qtpy.QtCore import QRectF, Qt
from qtpy.QtGui import QPainter, QColor

class EventNameItem(QGraphicsItem):
    def __init__(self, group, name):
        super().__init__()
        self._group = group
        self._name = name
        self._bg_brush = QColor(255,255,255,255)
        self._rect = QRectF(-20,-50,200,40)
        self.setZValue(100)

    ## UI EVENTS
    def boundingRect(self):
        return self._rect
    
    def paint(self, painter: QPainter, option, widget):
        
        label = f"{self._group}.{self._name}"
        
        font = painter.font()
        font.setPointSize(8)
        w = painter.fontMetrics().width(label)
        h = painter.fontMetrics().height()

        painter.setPen(Qt.red)
        painter.setBrush(self._bg_brush)
        self._rect = QRectF(0,-h-3,w+16,h+10)
        self.prepareGeometryChange()
        painter.drawRect(self._rect)

        painter.setPen(Qt.black)
        painter.setFont(font)
        painter.drawText(3, 0, label)
