#! /usr/bin/env python3
"""
    SSWDIntroStep
    Settings viewer of the intro plugin for the Slow Wave Detector tool
"""
import numpy as np
from qtpy import QtCore, QtGui, QtWidgets

from CEAMSTools.SlowWaveDetection.SSWDIntroStep.Ui_SSWDIntroStep import Ui_SSWDIntroStep
from commons.BaseStepView import BaseStepView

# Height of the illustration of a slow wave (pixels); it takes the width of its card
IMAGE_HEIGHT = 112


def simulated_eeg(seconds=5.0, fs=256, seed=7):
    """ A simulated EEG of N2 sleep: mixed frequencies, mostly 2-10 Hz (amplitudes in 1/f), with one
        slow wave in the middle (1 Hz): a negative half-wave followed by a smaller positive half-wave,
        from one zero crossing (positive to negative) to the next.
        Returns the time (s), the signal (unit standard deviation) and the mask of the slow wave.
    """
    rng = np.random.default_rng(seed)
    time = np.arange(int(seconds * fs)) / fs
    signal = np.zeros_like(time)
    for frequency in np.linspace(2.0, 10.0, 40):
        signal += rng.normal() / frequency * np.sin(2 * np.pi * frequency * time + rng.uniform(0, 2 * np.pi))
    noise = np.convolve(rng.normal(size=time.size), np.ones(3) / 3, mode="same")
    signal = 0.35 * signal / signal.std() + 0.04 * noise
    start, frequency = seconds / 2 - 0.5, 1.0
    wave = np.sin(2 * np.pi * frequency * (time - start))
    mask = (time >= start) & (time <= start + 1 / frequency)
    signal -= 3.0 * np.where(mask, np.where(wave > 0, wave, 0.7 * wave), 0.0)
    return time, signal / signal.std(), mask


def draw_slow_wave(painter, width, height, palette, font):
    """ Draw the illustration of a slow wave in a width x height area, in the colors of the theme
        (palette): the EEG in the text color, the slow wave in the link color on a light band, a 1 s scale.
    """
    time, signal, mask = simulated_eeg()
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

    wave = np.nonzero(mask)[0]
    start, end = x[wave[0]], x[wave[-1]]
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(band)
    painter.drawRoundedRect(QtCore.QRectF(start - 6, top - 4, end - start + 12, bottom - top + 8), 6, 6)

    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    painter.setPen(QtGui.QPen(muted, 1.2))
    painter.drawPath(path(np.arange(time.size)))
    painter.setPen(QtGui.QPen(link, 1.6))
    painter.drawPath(path(wave))

    painter.drawText(QtCore.QRectF(start - 6, 0, end - start + 120, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, "Slow wave")
    one_second = (right - left) / (time[-1] - time[0])
    scale_y = height - label_height / 2 - 1
    painter.setPen(QtGui.QPen(muted, 1.5))
    painter.drawLine(QtCore.QPointF(left, scale_y), QtCore.QPointF(left + one_second, scale_y))
    painter.drawText(QtCore.QRectF(left + one_second + 6, height - label_height - 1, 60, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, "1 s")


class SlowWaveDrawing(QtCore.QObject):
    """ Paints the illustration of a slow wave on its label, at the width of the label, when the label
        is painted: sharp on every screen and in the colors of the theme. The label has no picture,
        so the page does not put it in a picture card (made for pictures on a white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_slow_wave(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class SSWDIntroStep( BaseStepView,  Ui_SSWDIntroStep, QtWidgets.QWidget):
    """
        SSWDIntroStep
        Displays the functionnalities of the slow wave detector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The illustration of a slow wave (simulated EEG), painted on slow_wave_image
        self._slow_wave_drawing = SlowWaveDrawing(self.slow_wave_image)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
