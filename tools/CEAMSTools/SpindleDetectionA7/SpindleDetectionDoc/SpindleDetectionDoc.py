"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    Description of the tool to detect spindles with the a7 algorithm.
"""
import numpy as np
from qtpy import QtCore, QtGui, QtWidgets

from CEAMSTools.SpindleDetectionA7.SpindleDetectionDoc.Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView

# Height of the illustration of a spindle (pixels); it takes the width of its card
IMAGE_HEIGHT = 112


def simulated_eeg(seconds=5.0, fs=256, seed=11):
    """ A simulated EEG of N2 sleep: mixed frequencies, mostly 1-8 Hz (amplitudes in 1/f), with one
        sleep spindle in the middle (13 Hz, about 1.4 s, waxing and waning).
        Returns the time (s), the signal (unit standard deviation) and the envelope of the spindle (0-1).
    """
    rng = np.random.default_rng(seed)
    time = np.arange(int(seconds * fs)) / fs
    signal = np.zeros_like(time)
    for frequency in np.linspace(0.7, 9.0, 40):
        signal += rng.normal() / frequency * np.sin(2 * np.pi * frequency * time + rng.uniform(0, 2 * np.pi))
    noise = np.convolve(rng.normal(size=time.size), np.ones(3) / 3, mode="same")
    signal = signal / signal.std() + 0.12 * noise
    center, duration = seconds / 2, 1.4
    phase = (time - center) / duration
    envelope = np.where(np.abs(phase) < 0.5, np.cos(np.pi * phase) ** 2, 0.0)
    signal += 2.2 * envelope * np.sin(2 * np.pi * 13 * time)
    return time, signal / signal.std(), envelope


def draw_spindle(painter, width, height, palette, font):
    """ Draw the illustration of a spindle in a width x height area, in the colors of the theme
        (palette): the EEG in the text color, the spindle in the link color on a light band, a 1 s scale.
    """
    time, signal, envelope = simulated_eeg()
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    label_height = QtGui.QFontMetrics(small).height()
    left, right = 2.0, width - 2.0
    top, bottom = label_height + 6.0, height - label_height - 6.0
    x = left + (time - time[0]) / (time[-1] - time[0]) * (right - left)
    y = (top + bottom) / 2 - signal / np.abs(signal).max() * (bottom - top) / 2

    def path(indexes):
        trace = QtGui.QPainterPath(QtCore.QPointF(x[indexes[0]], y[indexes[0]]))
        for index in indexes[1:]:
            trace.lineTo(x[index], y[index])
        return trace

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    link = palette.color(QtGui.QPalette.ColorRole.Link)
    band = QtGui.QColor(link)
    band.setAlpha(30)

    spindle = np.nonzero(envelope > 0.02)[0]
    start, end = x[spindle[0]], x[spindle[-1]]
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(band)
    painter.drawRoundedRect(QtCore.QRectF(start - 6, top - 4, end - start + 12, bottom - top + 8), 6, 6)

    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    painter.setPen(QtGui.QPen(muted, 1.2))
    painter.drawPath(path(np.arange(time.size)))
    painter.setPen(QtGui.QPen(link, 1.6))
    painter.drawPath(path(spindle))

    painter.drawText(QtCore.QRectF(start - 6, 0, end - start + 120, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, "Sleep spindle")
    one_second = (right - left) / (time[-1] - time[0])
    scale_y = height - label_height / 2 - 1
    painter.setPen(QtGui.QPen(muted, 1.5))
    painter.drawLine(QtCore.QPointF(left, scale_y), QtCore.QPointF(left + one_second, scale_y))
    painter.drawText(QtCore.QRectF(left + one_second + 6, height - label_height - 1, 60, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, "1 s")


class SpindleDrawing(QtCore.QObject):
    """ Paints the illustration of a spindle on its label, at the width of the label, when the label
        is painted: sharp on every screen and in the colors of the theme. The label has no picture,
        so the page does not put it in a picture card (made for pictures on a white background).
        Also used by the introductions of Detect Spindles with Martin and with SUMO.
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_spindle(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        Description of the tool to detect spindles with the a7 algorithm.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._draw_spindle_image()

    def _draw_spindle_image(self):
        """ The illustration of a spindle (simulated EEG), painted on spindle_image. """
        self._spindle_drawing = SpindleDrawing(self.spindle_image)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
