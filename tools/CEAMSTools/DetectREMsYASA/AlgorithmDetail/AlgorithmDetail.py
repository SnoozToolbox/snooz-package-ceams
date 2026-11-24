#! /usr/bin/env python3
"""
    AlgorithmDetail
    Description of the algorithm used to detect REMs.
"""

import numpy as np
from qtpy import QtCore, QtGui, QtWidgets

from commons.BaseStepView import BaseStepView

from CEAMSTools.DetectREMsYASA.AlgorithmDetail.Ui_AlgorithmDetail import Ui_AlgorithmDetail

# Height of the illustration of the REM events (pixels); it takes the width of its card
IMAGE_HEIGHT = 176
# The rapid eye movements of the example: onset (s) and direction of the LOC deflection (+1 up, -1 down)
REMS = [(0.9, 1), (2.4, -1), (3.9, 1), (5.2, -1), (6.6, 1)]
# Duration of the highlighted part of a REM (s), from its onset
REM_DURATION = 0.7


def simulated_eog(seconds=7.6, fs=128, seed=3):
    """ A simulated EOG of REM sleep: the left (LOC) and right (ROC) channels, with rapid eye movements
        (a fast deflection and a slower return) in opposite directions on the two channels, a slow drift
        and some noise. Returns the time (s), LOC and ROC (in units of the REM amplitude).
    """
    rng = np.random.default_rng(seed)
    time = np.arange(int(seconds * fs)) / fs
    eyes = np.zeros_like(time)
    for onset, direction in REMS:
        after = np.clip(time - onset, 0, None)
        amplitude = direction * rng.uniform(0.8, 1.0)
        eyes += np.where(time >= onset, amplitude * (1 - np.exp(-after / 0.03)) * np.exp(-after / 0.3), 0.0)
    drift = 0.12 * np.sin(2 * np.pi * 0.21 * time + 0.6) + 0.06 * np.sin(2 * np.pi * 0.47 * time + 2.1)

    def noise():
        return 0.035 * np.convolve(rng.normal(size=time.size), np.ones(4) / 4, mode="same")

    return time, eyes + drift + noise(), -0.9 * (eyes + drift) + noise()


def draw_rems(painter, width, height, palette, font):
    """ Draw the illustration of the REM events in a width x height area, in the colors of the theme
        (palette): the LOC and ROC channels in the text color, each REM in the link color on a light band
        across both channels, with its label, and a 1 s scale.
    """
    time, loc, roc = simulated_eog()
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    metrics = QtGui.QFontMetrics(small)
    label_height = metrics.height()

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    link = palette.color(QtGui.QPalette.ColorRole.Link)
    band = QtGui.QColor(link)
    band.setAlpha(30)

    left = metrics.horizontalAdvance("LOC") + 10.0
    right = width - 2.0
    top = label_height + 6.0
    bottom = height - label_height - 6.0
    row = (bottom - top) / 2
    scale = max(np.abs(loc).max(), np.abs(roc).max())
    x = left + (time - time[0]) / (time[-1] - time[0]) * (right - left)

    def y_of(signal, index):
        center = top + row * (index + 0.5)
        return center - signal / scale * row * 0.46

    def path(signal, index, indexes):
        y = y_of(signal, index)
        trace = QtGui.QPainterPath(QtCore.QPointF(x[indexes[0]], y[indexes[0]]))
        for sample in indexes[1:]:
            trace.lineTo(x[sample], y[sample])
        return trace

    rem_samples = []
    for onset, _ in REMS:
        samples = np.nonzero((time >= onset - 0.05) & (time <= onset + REM_DURATION))[0]
        rem_samples.append(samples)
        start, end = x[samples[0]], x[samples[-1]]
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(band)
        painter.drawRoundedRect(QtCore.QRectF(start - 3, top - 2, end - start + 6, bottom - top + 4), 6, 6)
        painter.setPen(text)
        painter.drawText(QtCore.QRectF(start - 30, 0, end - start + 60, label_height),
                         QtCore.Qt.AlignmentFlag.AlignCenter, "REM")

    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    for index, (signal, name) in enumerate(((loc, "LOC"), (roc, "ROC"))):
        painter.setPen(QtGui.QPen(muted, 1.2))
        painter.drawPath(path(signal, index, np.arange(time.size)))
        painter.setPen(QtGui.QPen(link, 1.6))
        for samples in rem_samples:
            painter.drawPath(path(signal, index, samples))
        painter.setPen(muted)
        painter.drawText(QtCore.QRectF(0, top + row * (index + 0.5) - label_height / 2, left - 6, label_height),
                         QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, name)

    one_second = (right - left) / (time[-1] - time[0])
    scale_y = height - label_height / 2 - 1
    painter.setPen(QtGui.QPen(muted, 1.5))
    painter.drawLine(QtCore.QPointF(left, scale_y), QtCore.QPointF(left + one_second, scale_y))
    painter.drawText(QtCore.QRectF(left + one_second + 6, height - label_height - 1, 60, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, "1 s")


class RemDrawing(QtCore.QObject):
    """ Paints the illustration of the REM events on its label, at the width of the label, when the label
        is painted: sharp on every screen and in the colors of the theme. The label has no picture, so the
        page does not put it in a picture card (made for pictures on a white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_rems(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class AlgorithmDetail(BaseStepView, Ui_AlgorithmDetail, QtWidgets.QWidget):
    """
        AlgorithmDetail
        Description of the algorithm used to detect REMs.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The illustration of the REM events (simulated EOG), painted on label_2
        self._rem_drawing = RemDrawing(self.label_2)

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        pass

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        pass
        
    def on_apply_settings(self):
        # Slot called when the user wants to apply the settings
        pass
        
    # Slot called when the user wants to write the filename
    def on_choose(self):
        pass

    def on_active_validation(self):
        pass

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True

    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass
