"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""
from qtpy import QtCore, QtGui, QtWidgets

from CEAMSTools.SleepBouts.IntroStep.Ui_IntroStep import Ui_IntroStep
from commons.BaseStepView import BaseStepView

# Height of the illustration of the sleep bouts (pixels); it takes the width of its card
IMAGE_HEIGHT = 96
# The sleep stages of the example (one box per epoch) and its bouts: (first box, last box, name)
STAGES = ["W", "W", "W", "N1", "N2", "N2", "N3", "R", "R", "N1", "W"]
BOUTS_ABOVE = [(4, 6, "N2–N3"), (7, 8, "REM")]
BOUTS_BELOW = [(4, 8, "N2–N3–REM")]


def draw_sleep_bouts(painter, width, height, palette, font):
    """ Draw the illustration of the sleep bouts in a width x height area, in the colors of the theme
        (palette): the epochs of the example in boxes, the stages of the bouts on a light band of the
        link color (darker for R), each bout under a bracket of the link color.
    """
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    text_height = QtGui.QFontMetrics(small).height()

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    link = palette.color(QtGui.QPalette.ColorRole.Link)
    nrem_band = QtGui.QColor(link)
    nrem_band.setAlpha(40)
    rem_band = QtGui.QColor(link)
    rem_band.setAlpha(90)

    box_width = min(56.0, (width - 4.0) / len(STAGES))
    box_height = 28.0
    left = (width - box_width * len(STAGES)) / 2
    top = (height - box_height) / 2
    center = QtCore.Qt.AlignmentFlag.AlignCenter

    for index, stage in enumerate(STAGES):
        box = QtCore.QRectF(left + index * box_width, top, box_width, box_height)
        band = nrem_band if stage in ("N2", "N3") else rem_band if stage == "R" else None
        if band is not None:
            painter.fillRect(box, band)
        painter.setPen(QtGui.QPen(muted, 1))
        painter.drawRect(box)
        painter.setPen(text)
        painter.drawText(box, center, stage)

    def bracket(first, last, name, above):
        x1 = left + first * box_width + 3
        x2 = left + (last + 1) * box_width - 3
        y = top - 9 if above else top + box_height + 9
        tick = 5 if above else -5  # towards the boxes
        painter.setPen(QtGui.QPen(link, 1.5))
        painter.drawLine(QtCore.QPointF(x1, y), QtCore.QPointF(x2, y))
        painter.drawLine(QtCore.QPointF(x1, y), QtCore.QPointF(x1, y + tick))
        painter.drawLine(QtCore.QPointF(x2, y), QtCore.QPointF(x2, y + tick))
        text_top = y - text_height - 2 if above else y + 2
        painter.setPen(text)
        painter.drawText(QtCore.QRectF(x1 - 40, text_top, x2 - x1 + 80, text_height), center, name)

    for first, last, name in BOUTS_ABOVE:
        bracket(first, last, name, above=True)
    for first, last, name in BOUTS_BELOW:
        bracket(first, last, name, above=False)


class SleepBoutsDrawing(QtCore.QObject):
    """ Paints the illustration of the sleep bouts on its label, at the width of the label, when the
        label is painted: sharp on every screen and in the colors of the theme. The label has no
        picture, so the page does not put it in a picture card (made for pictures on a white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_sleep_bouts(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class IntroStep( BaseStepView,  Ui_IntroStep, QtWidgets.QWidget):
    """
        IntroStep describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The illustration of the sleep bouts, painted on label_5
        self._bouts_drawing = SleepBoutsDrawing(self.label_5)

    def load_settings(self):
        pass

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        pass

    def on_apply_settings(self):
        pass

    def on_validate_settings(self):
        return True
