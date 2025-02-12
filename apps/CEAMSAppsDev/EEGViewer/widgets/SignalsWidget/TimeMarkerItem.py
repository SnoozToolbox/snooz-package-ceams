"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem
from qtpy.QtCore import QRectF, Qt
from qtpy.QtGui import QPainter

class TimeMarkerItem(QGraphicsItem):
    def __init__(self):
        super().__init__()

    def boundingRect(self):
        w = 50
        h = 2000
        x = -1
        y = -1
        return QRectF(x,y,w,h)
    

    def paint(self, painter: QPainter, option, widget):
        painter.setPen(Qt.lightGray)
        painter.drawLine(0,0,0,2000)
        painter.drawText(5,13,f"{self.data(0)}s")
        
        return None
