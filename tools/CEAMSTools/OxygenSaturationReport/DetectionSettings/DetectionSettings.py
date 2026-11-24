#! /usr/bin/env python3
"""
    DetectionSettings
    Class step to define the parameters of the oxygen desaturation.
    The Settings view is used to buil a dictionary to provide to the 
    oxygen desaturation detector.
"""
import numpy as np
from qtpy import QtCore, QtGui, QtWidgets

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.OxygenSaturationReport.DetectionSettings.Ui_DetectionSettings import Ui_DetectionSettings

# Height of the illustration of a desaturation (pixels)
IMAGE_HEIGHT = 190
# Maximum width of the illustration (pixels): it takes the width of its card up to this width
IMAGE_WIDTH = 640
# The example (s and %): the desaturation from Lmax to Lmin, then the recovery
LMAX_TIME, LMIN_TIME, RECOVERY_END = 22.0, 46.0, 58.0
LMAX_LEVEL, LMIN_LEVEL = 95.3, 91.0


def simulated_spo2(seconds=80.0, fs=4, seed=2):
    """ A simulated oxygen saturation (%) with one desaturation, from its maximum (Lmax) to its minimum
        (Lmin), followed by its recovery, around a stable level with small variations.
        Returns the time (s) and the saturation (%).
    """
    rng = np.random.default_rng(seed)
    time = np.arange(int(seconds * fs) + 1) / fs

    def smooth(start, end):  # 0 before start, 1 after end, smooth in between
        ratio = np.clip((time - start) / (end - start), 0, 1)
        return ratio * ratio * (3 - 2 * ratio)

    baseline = 95.0 + 0.25 * np.sin(2 * np.pi * time / 17.0) + 0.1 * np.sin(2 * np.pi * time / 6.0 + 1.0)
    peak = (LMAX_LEVEL - 95.0) * np.exp(-((time - LMAX_TIME) / 3.0) ** 2)
    drop = (LMAX_LEVEL - LMIN_LEVEL) * (smooth(LMAX_TIME, LMIN_TIME) - smooth(LMIN_TIME, RECOVERY_END))
    noise = 0.08 * np.convolve(rng.normal(size=time.size), np.ones(3) / 3, mode="same")
    return time, baseline + peak - drop + noise


def draw_desaturation(painter, width, height, palette, font):
    """ Draw the illustration of a desaturation in a width x height area, in the colors of the theme
        (palette): the oxygen saturation in the text color, the desaturation in the link color on a light
        band, with its drop (3 or 4%) and its duration, the recovery on a lighter band, a 10 s scale.
    """
    time, spo2 = simulated_spo2()
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    metrics = QtGui.QFontMetrics(small)
    label_height = metrics.height()

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    faint = QtGui.QColor(text)
    faint.setAlpha(70)
    link = palette.color(QtGui.QPalette.ColorRole.Link)
    band = QtGui.QColor(link)
    band.setAlpha(30)
    light_band = QtGui.QColor(link)
    light_band.setAlpha(14)

    area = min(float(width), IMAGE_WIDTH)
    left, right = 2.0, area - 2.0
    top = label_height + 8.0
    arrow_y = height - label_height - 12.0
    bottom = arrow_y - 12.0
    low, high = 90.2, 96.0

    def x_of(seconds):
        return left + (seconds - time[0]) / (time[-1] - time[0]) * (right - left)

    def y_of(level):
        return bottom - (level - low) / (high - low) * (bottom - top)

    def path(indexes):
        trace = QtGui.QPainterPath(QtCore.QPointF(x_of(time[indexes[0]]), y_of(spo2[indexes[0]])))
        for index in indexes[1:]:
            trace.lineTo(x_of(time[index]), y_of(spo2[index]))
        return trace

    def text_at(rect, value, flags, color):
        painter.setPen(color)
        painter.drawText(rect, flags, value)

    center = QtCore.Qt.AlignmentFlag.AlignCenter
    lmax = int(np.argmin(np.abs(time - LMAX_TIME)))
    lmin = int(np.argmin(np.abs(time - LMIN_TIME)))
    lmax = lmax - 8 + int(np.argmax(spo2[lmax - 8:lmax + 9]))
    lmin = lmin - 8 + int(np.argmin(spo2[lmin - 8:lmin + 9]))
    x_max, x_min, x_end = x_of(time[lmax]), x_of(time[lmin]), x_of(RECOVERY_END)
    y_max, y_min = y_of(spo2[lmax]), y_of(spo2[lmin])

    # The bands of the desaturation and of the recovery, with their names
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(band)
    painter.drawRoundedRect(QtCore.QRectF(x_max, top - 4, x_min - x_max, bottom - top + 8), 6, 6)
    painter.setBrush(light_band)
    painter.drawRoundedRect(QtCore.QRectF(x_min, top - 4, x_end - x_min, bottom - top + 8), 6, 6)
    text_at(QtCore.QRectF(x_max - 20, 0, x_min - x_max + 40, label_height), "Desaturation", center, text)
    text_at(QtCore.QRectF(x_min - 20, 0, x_end - x_min + 40, label_height), "Recovery", center, muted)
    text_at(QtCore.QRectF(left, 0, 80, label_height), "SpO2 (%)",
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, muted)

    # The drop: the levels of Lmax and Lmin, and an arrow between them before the desaturation
    drop_x = x_max - 14
    painter.setPen(QtGui.QPen(faint, 1.0, QtCore.Qt.PenStyle.DashLine))
    painter.drawLine(QtCore.QPointF(drop_x - 6, y_max), QtCore.QPointF(x_max, y_max))
    painter.drawLine(QtCore.QPointF(drop_x - 6, y_min), QtCore.QPointF(x_min, y_min))
    # The duration: guides from Lmax and Lmin down to its arrow
    painter.setPen(QtGui.QPen(faint, 1.0, QtCore.Qt.PenStyle.DotLine))
    painter.drawLine(QtCore.QPointF(x_max, y_max), QtCore.QPointF(x_max, arrow_y))
    painter.drawLine(QtCore.QPointF(x_min, y_min), QtCore.QPointF(x_min, arrow_y))

    # The saturation, the desaturation in the link color, Lmax and Lmin
    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    painter.setPen(QtGui.QPen(muted, 1.4))
    painter.drawPath(path(np.arange(time.size)))
    painter.setPen(QtGui.QPen(link, 2.2))
    painter.drawPath(path(np.arange(lmax, lmin + 1)))
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(text)
    for point in (QtCore.QPointF(x_max, y_max), QtCore.QPointF(x_min, y_min)):
        painter.drawEllipse(point, 3.5, 3.5)
    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)

    def arrow(x1, y1, x2, y2):
        painter.drawLine(QtCore.QPointF(x1, y1), QtCore.QPointF(x2, y2))
        vertical = x1 == x2
        for (tip_x, tip_y), direction in (((x1, y1), 1), ((x2, y2), -1)):
            if vertical:
                painter.drawLine(QtCore.QPointF(tip_x, tip_y), QtCore.QPointF(tip_x - 4, tip_y + 6 * direction))
                painter.drawLine(QtCore.QPointF(tip_x, tip_y), QtCore.QPointF(tip_x + 4, tip_y + 6 * direction))
            else:
                painter.drawLine(QtCore.QPointF(tip_x, tip_y), QtCore.QPointF(tip_x + 6 * direction, tip_y - 4))
                painter.drawLine(QtCore.QPointF(tip_x, tip_y), QtCore.QPointF(tip_x + 6 * direction, tip_y + 4))

    painter.setPen(QtGui.QPen(text, 1.2))
    arrow(drop_x, y_max, drop_x, y_min)
    arrow(x_max, arrow_y, x_min, arrow_y)
    right_flags = QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter
    middle = (y_max + y_min) / 2
    text_at(QtCore.QRectF(drop_x - 126, middle - label_height, 120, label_height), "Drop", right_flags, text)
    text_at(QtCore.QRectF(drop_x - 126, middle, 120, label_height), "3 or 4%", right_flags, text)
    text_at(QtCore.QRectF(x_max - 60, arrow_y + 2, x_min - x_max + 120, label_height),
            "Desaturation duration", center, text)

    # A 10 s scale, at the bottom right
    ten_seconds = 10.0 / (time[-1] - time[0]) * (right - left)
    scale_y = height - label_height / 2 - 1
    label_width = metrics.horizontalAdvance("10 s") + 6
    painter.setPen(QtGui.QPen(muted, 1.5))
    painter.drawLine(QtCore.QPointF(right - label_width - ten_seconds, scale_y),
                     QtCore.QPointF(right - label_width, scale_y))
    text_at(QtCore.QRectF(right - label_width + 6, height - label_height - 1, label_width, label_height), "10 s",
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, muted)


class DesaturationDrawing(QtCore.QObject):
    """ Paints the illustration of a desaturation on its label, at the width of the label (up to
        IMAGE_WIDTH), when the label is painted: sharp on every screen and in the colors of the theme.
        The label has no picture, so the page does not put it in a picture card (made for pictures on a
        white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_desaturation(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class DetectionSettings(BaseStepView, Ui_DetectionSettings, QtWidgets.QWidget):
    """
        DetectionSettings
        Class step to define the parameters of the oxygen desaturation.
        The Settings view is used to buil a dictionary to provide to the 
        oxygen desaturation detector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The illustration of a desaturation (simulated oxygen saturation), painted on label_pic
        self._desaturation_drawing = DesaturationDrawing(self.label_pic)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_DetectionSettings"] = {"the_data_I_want_to_share":"some_data"}
        self.parameters_oxy = {}
        self._node_id_oxy_det = "88a51ed5-da37-457f-8e32-221b0a600195"
        self._oxy_topic = f'{self._node_id_oxy_det}.parameters_oxy'
        self._pub_sub_manager.subscribe(self, self._oxy_topic)
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.

        # You need to look into your process.json file to know the ID of the node
        # you are interest in
        self._pub_sub_manager.publish(self, self._oxy_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._oxy_topic:
            if isinstance(message, str):
                self.parameters_oxy = eval(message)
                if self.parameters_oxy['desaturation_drop_percent']==3:
                    self.radioButton_3perc.setChecked(True)
                else:
                    self.radioButton_4perc.setChecked(True)
                if self.parameters_oxy['max_slope_drop_sec']==180:
                    self.radioButton_180s.setChecked(True)
                else:
                    self.radioButton_20s.setChecked(True)                
                if self.parameters_oxy['min_hold_drop_sec']==10:
                    self.radioButton_hold_10s.setChecked(True)
                else:
                    self.radioButton_hold_5s.setChecked(True)


    def on_apply_settings(self):
        if self.radioButton_3perc.isChecked():
            self.parameters_oxy['desaturation_drop_percent'] = 3
        elif self.radioButton_4perc.isChecked():
            self.parameters_oxy['desaturation_drop_percent'] = 4
        if self.radioButton_180s.isChecked():
            self.parameters_oxy['max_slope_drop_sec'] = 180
        elif self.radioButton_20s.isChecked():
            self.parameters_oxy['max_slope_drop_sec'] = 20        
        if self.radioButton_hold_10s.isChecked():
            self.parameters_oxy['min_hold_drop_sec'] = 10
        elif self.radioButton_hold_5s.isChecked():
            self.parameters_oxy['min_hold_drop_sec'] = 5     
        self._pub_sub_manager.publish(self, self._oxy_topic, str(self.parameters_oxy)) 


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True
