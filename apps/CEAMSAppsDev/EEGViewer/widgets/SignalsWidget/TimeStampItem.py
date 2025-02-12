"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QGraphicsItem
from qtpy.QtCore import Slot, QRectF, Qt
from qtpy.QtGui import QPainter

class TimeStampItem(QGraphicsItem):
    def __init__(self):
        super().__init__()
        self._start_time = 0
        self._time_offset = 0
        self._left_padding = 50
        self._display_height = 0
        self._display_width = 0

    def boundingRect(self):
        w = 100
        h = 40
        x = 0
        y = -20
        return QRectF(x,y,w,h)
    
    @Slot()
    def on_parent_resize(self, width, height):
        # This method is called whenever the widget is resized
        self._display_height = height
        self._display_width = width
        pos = self.pos()
        pos.setY(self._display_height - 20)
        pos.setX(self._left_padding)
        self.setPos(pos)
        self.update()

    def paint(self, painter: QPainter, option, widget):
        painter.setPen(Qt.lightGray)
        painter.setPen(Qt.black)
        font = painter.font()
        font.setPointSize(16)
        painter.setFont(font)
        painter.drawText(5,0, f"{self._start_time + self._time_offset} sec.")

        line_pen = painter.pen()
        line_pen.setColor(Qt.black)  # Set the color (black in this example)
        line_pen.setWidth(3)  # Set the line width (3 in this example)
        painter.setPen(line_pen)
        painter.drawLine(0, -30, 0, 0)

    @Slot()
    def on_time_offset_change(self, time_offset):
        self._time_offset = time_offset
        self.update()
