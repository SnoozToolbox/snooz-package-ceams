#! /usr/bin/env python3
"""
    SSWDCriterias
    Settings viewer of the save files plugin for the Slow Wave Detector tool
"""
import math

from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

from CEAMSTools.SlowWaveDetection.SSWDCriterias.Ui_SSWDCriterias import Ui_SSWDCriterias
from commons.BaseStepView import BaseStepView

# Size of the drawing of the phase of a slow wave (pixels): at most PHASE_WIDTH wide, left aligned
PHASE_HEIGHT = 224
PHASE_WIDTH = 440


def draw_phase(painter, width, height, palette, font):
    """ Draw one slow wave and its phase (Bouchard et al., 2021, figure 1A) in the colors of the theme
        (palette): from a zero crossing, positive to negative (-3pi/2), to the next one (+pi/2), with the
        negative peak H (hyperpolarization, -pi), the positive peak D (depolarization, 0), the duration T
        of the wave and the time tau from H to D. The transition from H to D is in the link color.
    """
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    label_height = QtGui.QFontMetrics(small).height()

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    faint = QtGui.QColor(text)
    faint.setAlpha(70)
    link = palette.color(QtGui.QPalette.ColorRole.Link)

    # The wave: phase -3pi/2 .. pi/2 (value cos(phase)), the times of the knots in fractions of T
    area = min(width, PHASE_WIDTH)
    start_x, end_x = 52.0, area - 52.0
    phases = [-1.5 * math.pi, -math.pi, 0.0, 0.5 * math.pi]
    times = [0.0, 0.24, 0.72, 1.0]
    d_y = label_height + 8.0                      # positive peak D
    zero_y = d_y + 46.0
    h_y = zero_y + 62.0                           # negative peak H
    tau_y = h_y + label_height + 26.0             # arrow of tau
    t_y = height - 6.0                            # arrow of T

    def x_of(phase):
        for index in range(len(phases) - 1):
            if phase <= phases[index + 1]:
                ratio = (phase - phases[index]) / (phases[index + 1] - phases[index])
                fraction = times[index] + ratio * (times[index + 1] - times[index])
                return start_x + fraction * (end_x - start_x)
        return end_x

    def point(phase):
        value = math.cos(phase)
        return QtCore.QPointF(x_of(phase), zero_y - value * ((zero_y - d_y) if value > 0 else (h_y - zero_y)))

    def trace(first, last, count=120):
        path = QtGui.QPainterPath(point(first))
        for index in range(1, count + 1):
            path.lineTo(point(first + (last - first) * index / count))
        return path

    def arrow(x1, x2, y):
        painter.drawLine(QtCore.QPointF(x1, y), QtCore.QPointF(x2, y))
        for tip, direction in ((x1, 1), (x2, -1)):
            painter.drawLine(QtCore.QPointF(tip, y), QtCore.QPointF(tip + 6 * direction, y - 4))
            painter.drawLine(QtCore.QPointF(tip, y), QtCore.QPointF(tip + 6 * direction, y + 4))

    def text_at(x, y, value, align):
        left = {"left": x, "right": x - 160, "center": x - 80}[align]
        flags = {"left": QtCore.Qt.AlignmentFlag.AlignLeft, "right": QtCore.Qt.AlignmentFlag.AlignRight,
                 "center": QtCore.Qt.AlignmentFlag.AlignHCenter}[align]
        painter.drawText(QtCore.QRectF(left, y - label_height / 2, 160, label_height),
                         flags | QtCore.Qt.AlignmentFlag.AlignVCenter, value)

    h, d = point(-math.pi), point(0.0)
    # Zero line and guides
    painter.setPen(QtGui.QPen(faint, 1.0, QtCore.Qt.PenStyle.DashLine))
    painter.drawLine(QtCore.QPointF(start_x - 12, zero_y), QtCore.QPointF(end_x + 12, zero_y))
    painter.setPen(QtGui.QPen(faint, 1.0, QtCore.Qt.PenStyle.DotLine))
    for x in (start_x, end_x):
        painter.drawLine(QtCore.QPointF(x, zero_y), QtCore.QPointF(x, t_y))
    painter.drawLine(QtCore.QPointF(h.x(), h.y() + label_height + 4), QtCore.QPointF(h.x(), tau_y))
    painter.drawLine(QtCore.QPointF(d.x(), d.y()), QtCore.QPointF(d.x(), tau_y))
    # The wave, the transition from H to D in the link color
    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    painter.setPen(QtGui.QPen(muted, 2.0))
    painter.drawPath(trace(phases[0], phases[-1], 240))
    painter.setPen(QtGui.QPen(link, 3.0))
    painter.drawPath(trace(-math.pi, 0.0))
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(text)
    for center, radius in ((h, 4.0), (d, 4.0), (point(phases[0]), 3.0), (point(phases[-1]), 3.0)):
        painter.drawEllipse(center, radius, radius)
    # Labels and arrows
    painter.setPen(QtGui.QPen(text, 1.2))
    text_at(d.x(), d.y() - label_height / 2 - 4, "D (0)", "center")
    text_at(h.x(), h.y() + label_height / 2 + 4, "H (−π)", "center")
    text_at(start_x - 8, zero_y, "−3π/2", "right")
    text_at(end_x + 8, zero_y, "+π/2", "left")
    arrow(h.x(), d.x(), tau_y)
    text_at((h.x() + d.x()) / 2, tau_y - label_height / 2 - 2, "τ", "center")
    arrow(start_x, end_x, t_y)
    text_at((start_x + end_x) / 2, t_y - label_height / 2 - 2, "T", "center")


class PhaseDrawing(QtCore.QObject):
    """ Paints the phase of a slow wave on its label (pages Detection Criteria and Output Files), when
        the label is painted: sharp on every screen and in the colors of the theme. The label has no
        picture, so the page does not put it in a picture card (made for pictures on a white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(PHASE_HEIGHT)
        label.setMaximumHeight(PHASE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_phase(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)

class SSWDCriterias( BaseStepView,  Ui_SSWDCriterias, QtWidgets.QWidget):
    """
        SSWDCriterias
        Displays the next steps for the selection of the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The phase of a slow wave (H, D, T and tau of the criteria), painted on phase_image
        self._phase_drawing = PhaseDrawing(self.phase_image)

        # Set input validators
        # Create a QRegularExpressionValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegularExpression(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s_-]*$')
        validator = QRegularExpressionValidator(regex)

        # Set the validator for the QLineEdit
        self.event_name_lineedit.setValidator(validator)
        self.event_name_lineedit.setMaxLength(64)
        self.group_lineedit.setValidator(validator)
        self.group_lineedit.setMaxLength(64)
        
        # Define modules and nodes to talk to
        self._node_id_SlowWaveDetector = "b96c5849-1c9c-4b54-8965-c63ecf2fb2b6"
        self._node_id_SleepStageEvents = "724a65d7-444b-4fe2-b62b-e8004906da4a"
        self._node_id_discard_events1 = "c0153cbd-cab8-4c43-8555-3585b48f7248"
        self._node_id_discard_events2 = "0b3bd08b-6b82-4c72-8968-a0c33552e5fb"
        self._node_id_SWDetails = "0308c274-4216-4642-9093-0ac919e9a0de"

        self._stages_topic = f'{self._node_id_SleepStageEvents}.stages'
        self._exclude_remp_topic = f'{self._node_id_SleepStageEvents}.exclude_remp'
        self._pub_sub_manager.subscribe(self, self._exclude_remp_topic)
        self._group_topic = f'{self._node_id_SlowWaveDetector}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_SlowWaveDetector}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._f_min_topic = f'{self._node_id_SlowWaveDetector}.f_min'
        self._pub_sub_manager.subscribe(self, self._f_min_topic)
        self._f_max_topic = f'{self._node_id_SlowWaveDetector}.f_max'
        self._pub_sub_manager.subscribe(self, self._f_max_topic)
        self._th_PaP_topic = f'{self._node_id_SlowWaveDetector}.th_PaP'
        self._pub_sub_manager.subscribe(self, self._th_PaP_topic)
        self._th_Neg_topic = f'{self._node_id_SlowWaveDetector}.th_Neg'
        self._pub_sub_manager.subscribe(self, self._th_Neg_topic)
        self._min_tNe_topic = f'{self._node_id_SlowWaveDetector}.min_tNe'
        self._pub_sub_manager.subscribe(self, self._min_tNe_topic)
        self._max_tNe_topic = f'{self._node_id_SlowWaveDetector}.max_tNe'
        self._pub_sub_manager.subscribe(self, self._max_tNe_topic)
        self._min_tPo_topic = f'{self._node_id_SlowWaveDetector}.min_tPo'
        self._pub_sub_manager.subscribe(self, self._min_tPo_topic)
        self._max_tPo_topic = f'{self._node_id_SlowWaveDetector}.max_tPo'
        self._pub_sub_manager.subscribe(self, self._max_tPo_topic)
        self._age_criterion_topic = f'{self._node_id_SlowWaveDetector}.age_criterion'
        self._pub_sub_manager.subscribe(self, self._age_criterion_topic)
        self._years_topic = f'{self._node_id_SlowWaveDetector}.years'
        self._pub_sub_manager.subscribe(self, self._years_topic)
        self._months_topic = f'{self._node_id_SlowWaveDetector}.months'
        self._pub_sub_manager.subscribe(self, self._months_topic)
        self._sex_criterion_topic = f'{self._node_id_SlowWaveDetector}.sex_criterion'
        self._pub_sub_manager.subscribe(self, self._sex_criterion_topic)
        self._sex_topic = f'{self._node_id_SlowWaveDetector}.sex'
        self._pub_sub_manager.subscribe(self, self._sex_topic)

        self._det_param_topic = f'{self._node_id_SWDetails}.slow_wave_det_param'
        self._pub_sub_manager.subscribe(self, self._det_param_topic)

        self._group1_topic = f'{self._node_id_discard_events1}.event_group'
        self._pub_sub_manager.subscribe(self, self._group1_topic)
        self._name1_topic = f'{self._node_id_discard_events1}.event_name'
        self._pub_sub_manager.subscribe(self, self._name1_topic)
        self._group2_topic = f'{self._node_id_discard_events2}.event_group'
        self._pub_sub_manager.subscribe(self, self._group2_topic)
        self._name2_topic = f'{self._node_id_discard_events2}.event_name'
        self._pub_sub_manager.subscribe(self, self._name2_topic)

        # Connect checkBox_r signal to update radioButton_incl_remp
        self.checkBox_r.toggled.connect(self.on_checkBox_r_toggled)


    def on_input_format_changed(self, int):
        if self.checkBox_age.isChecked():
            self.spinBox_years.setEnabled(True)
            self.label_years.setEnabled(True)
            self.spinBox_months.setEnabled(True)
            self.label_months.setEnabled(True)
        else:
            self.spinBox_years.setEnabled(False)
            self.label_years.setEnabled(False)
            self.spinBox_months.setEnabled(False)
            self.label_months.setEnabled(False)

        if self.checkBox_sex.isChecked():
            self.comboBox_sex.setEnabled(True)
        else:
            self.comboBox_sex.setEnabled(False)

        if self.carrier_radioButton.isChecked():
            self.doubleSpinBox_f_min.setValue(0.16)
            self.doubleSpinBox_f_min.setEnabled(False)
            self.doubleSpinBox_f_max.setValue(4.0)
            self.doubleSpinBox_f_max.setEnabled(False)
            self.doubleSpinBox_PaP_amp.setValue(75.0)
            self.doubleSpinBox_PaP_amp.setEnabled(False)
            self.doubleSpinBox_neg_amp.setValue(40.0)
            self.doubleSpinBox_neg_amp.setEnabled(False)
            self.spinBox_min_neg.setValue(125)
            self.spinBox_min_neg.setEnabled(False)
            self.spinBox_max_neg.setValue(1500)
            self.spinBox_max_neg.setEnabled(False)
            self.spinBox_min_pos.setValue(0)
            self.spinBox_min_pos.setEnabled(False)
            self.spinBox_max_pos.setValue(1000)
            self.spinBox_max_pos.setEnabled(False)
        
        if self.personalized_radioButton.isChecked():
            self.doubleSpinBox_f_min.setEnabled(True)
            self.doubleSpinBox_f_max.setEnabled(True)
            self.doubleSpinBox_PaP_amp.setEnabled(True)
            self.doubleSpinBox_neg_amp.setEnabled(True)
            self.spinBox_min_neg.setEnabled(True)
            self.spinBox_max_neg.setEnabled(True)
            self.spinBox_min_pos.setEnabled(True)
            self.spinBox_max_pos.setEnabled(True)

    def on_stage_mode_changed(self):
        """Handle changes to the sleep stage mode (Sleep Stages vs Unscored)."""
        if self.radioButton_sleep_stages.isChecked():
            # Sleep Stages mode: enable stage checkboxes
            self.checkBox_n1.setEnabled(True)
            self.checkBox_n2.setEnabled(True)
            self.checkBox_n3.setEnabled(True)
            self.checkBox_r.setEnabled(True)
            self.radioButton_excl_remp.setEnabled(True)
            self.radioButton_incl_remp.setEnabled(True)
            self.radioButton_excl_remp.setChecked(True)
        else:
            # Unscored mode: disable and uncheck stage checkboxes
            self.checkBox_n1.setEnabled(False)
            self.checkBox_n1.setChecked(False)
            self.checkBox_n2.setEnabled(False)
            self.checkBox_n2.setChecked(False)
            self.checkBox_n3.setEnabled(False)
            self.checkBox_n3.setChecked(False)
            self.checkBox_r.setEnabled(False)
            self.checkBox_r.setChecked(False)
            self.radioButton_incl_remp.setEnabled(False)
            self.radioButton_incl_remp.setChecked(True)
            self.radioButton_excl_remp.setEnabled(False)
            self.radioButton_excl_remp.setChecked(False)

    def on_checkBox_r_toggled(self, checked):
        """When checkBox_r (REM stage) is checked, automatically check radioButton_incl_remp."""
        if checked:
            self.radioButton_incl_remp.setChecked(True)

    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._f_min_topic, 'ping')
        self._pub_sub_manager.publish(self, self._f_max_topic, 'ping')
        self._pub_sub_manager.publish(self, self._th_PaP_topic, 'ping')
        self._pub_sub_manager.publish(self, self._th_Neg_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._min_tNe_topic, 'ping')
        self._pub_sub_manager.publish(self, self._max_tNe_topic, 'ping')
        self._pub_sub_manager.publish(self, self._min_tPo_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._max_tPo_topic, 'ping')
        self._pub_sub_manager.publish(self, self._age_criterion_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._years_topic, 'ping')
        self._pub_sub_manager.publish(self, self._months_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sex_criterion_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sex_topic, 'ping')


    def on_apply_settings(self):
        # Sleep stage selection to send to the "Sleep Stage Events" plugin
        stages_str = ''
        
        # Check if Unscored mode is selected
        if self.radioButton_unscored_mode.isChecked():
            stages_str = '9'
        else:
            # Sleep Stages mode: collect selected stages
            if self.checkBox_n1.isChecked():
                if len(stages_str)==0:
                    stages_str = '1'
                else:
                    stages_str = stages_str+',1'
            if self.checkBox_n2.isChecked():
                if len(stages_str)==0:
                    stages_str = '2'
                else:
                    stages_str = stages_str+',2'
            if self.checkBox_n3.isChecked():
                if len(stages_str)==0:
                    stages_str = '3'
                else:
                    stages_str = stages_str+',3'   
            if self.checkBox_r.isChecked():
                if len(stages_str)==0:
                    stages_str = '5'
                else:
                    stages_str = stages_str+',5'
        self._pub_sub_manager.publish(self, self._stages_topic, str(stages_str))
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, str(int(self.radioButton_excl_remp.isChecked())))
        # Send the settings to the publisher for inputs to SlowWaveDetector
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name_topic, \
            str(self.event_name_lineedit.text()))            
        self._pub_sub_manager.publish(self, self._f_min_topic, \
            str(self.doubleSpinBox_f_min.value()))
        self._pub_sub_manager.publish(self, self._f_max_topic, \
            str(self.doubleSpinBox_f_max.value()))
        self._pub_sub_manager.publish(self, self._th_PaP_topic, \
            str(self.doubleSpinBox_PaP_amp.value()))
        self._pub_sub_manager.publish(self, self._th_Neg_topic, \
            str(self.doubleSpinBox_neg_amp.value()))
        self._pub_sub_manager.publish(self, self._min_tNe_topic, \
            str(self.spinBox_min_neg.value()))
        self._pub_sub_manager.publish(self, self._max_tNe_topic, \
            str(self.spinBox_max_neg.value()))
        self._pub_sub_manager.publish(self, self._min_tPo_topic, \
            str(self.spinBox_min_pos.value()))
        self._pub_sub_manager.publish(self, self._max_tPo_topic, \
            str(self.spinBox_max_pos.value()))
        self._pub_sub_manager.publish(self, self._age_criterion_topic, \
            str(self.checkBox_age.isChecked()))
        self._pub_sub_manager.publish(self, self._years_topic, \
            str(self.spinBox_years.value()))
        self._pub_sub_manager.publish(self, self._months_topic, \
            str(self.spinBox_months.value()))
        self._pub_sub_manager.publish(self, self._sex_criterion_topic, \
            str(self.checkBox_sex.isChecked()))
        self._pub_sub_manager.publish(self, self._sex_topic, \
            str(self.comboBox_sex.currentText()))

        # Build the dictionary of section selection to run detector and the detector parameters
        det_param = {}
        det_param["stage_sel"] = stages_str
        det_param["detect_excl_remp"] = int(self.radioButton_excl_remp.isChecked())
        det_param["sw_event_name"] = str(self.event_name_lineedit.text())
        det_param['filt_low_Hz'] = self.doubleSpinBox_f_min.value()
        det_param['filt_high_Hz'] = self.doubleSpinBox_f_max.value()
        det_param['min_amp_pkpk_uV'] = self.doubleSpinBox_PaP_amp.value()
        det_param['min_neg_amp_uV'] = self.doubleSpinBox_neg_amp.value()
        det_param['min_neg_ms'] = self.spinBox_min_neg.value()
        det_param['max_neg_ms'] = self.spinBox_max_neg.value()
        det_param['min_pos_ms'] = self.spinBox_min_pos.value()
        det_param['max_pos_ms'] = self.spinBox_max_pos.value()

        self._pub_sub_manager.publish(self, self._det_param_topic, str(det_param))

        # To discard events during artifact 
        # (even if ther are resetted before the detection,
        # because we see uge artifact causing problems
        self._pub_sub_manager.publish(self, self._group1_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name1_topic, \
            str(self.event_name_lineedit.text()))  
        self._pub_sub_manager.publish(self, self._group2_topic, \
            str(self.group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._name2_topic, \
            str(self.event_name_lineedit.text()))          

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._stages_topic:
            stages_lst = message.split(',')
            # Check if unscored mode
            if '9' in stages_lst:
                self.radioButton_unscored_mode.setChecked(True)
                # Call the handler to update UI
                self.on_stage_mode_changed()
            else:
                self.radioButton_sleep_stages.setChecked(True)
                # Call the handler to update UI
                self.on_stage_mode_changed()
                # Check the corresponding stage checkboxes
                self.checkBox_n1.setChecked('1' in stages_lst)
                self.checkBox_n2.setChecked('2' in stages_lst)
                self.checkBox_n3.setChecked('3' in stages_lst)
                self.checkBox_r.setChecked('5' in stages_lst)
        if topic == self._exclude_remp_topic:
            self.radioButton_excl_remp.setChecked(int(message))
        if topic == self._group_topic:
            self.group_lineedit.setText(str(message))
        if topic == self._name_topic:
            self.event_name_lineedit.setText(str(message))
        if topic == self._f_min_topic:
            self.doubleSpinBox_f_min.setValue(float(message))
        if topic == self._f_max_topic:
            self.doubleSpinBox_f_max.setValue(float(message))
        if topic == self._th_PaP_topic:
            self.doubleSpinBox_PaP_amp.setValue(float(message))
        if topic == self._th_Neg_topic:
            self.doubleSpinBox_neg_amp.setValue(float(message))
        if topic == self._min_tNe_topic:
            self.spinBox_min_neg.setValue(int(message))
        if topic == self._max_tNe_topic:
            self.spinBox_max_neg.setValue(int(message))
        if topic == self._min_tPo_topic:
            self.spinBox_min_pos.setValue(int(message)) 
        if topic == self._max_tPo_topic:
            self.spinBox_max_pos.setValue(int(message)) 
        if topic == self._age_criterion_topic:
            self.checkBox_age.setChecked(eval(message))
        if topic == self._years_topic:
            self.spinBox_years.setValue(int(message))
        if topic == self._months_topic:
            self.spinBox_months.setValue(int(message))
        if topic == self._sex_criterion_topic:
            self.checkBox_sex.setChecked(eval(message))
        if topic == self._sex_topic:
            self.comboBox_sex.setCurrentText(message)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_topic)
            self._pub_sub_manager.unsubscribe(self, self._exclude_remp_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name_topic)   
            self._pub_sub_manager.unsubscribe(self, self._f_min_topic)
            self._pub_sub_manager.unsubscribe(self, self._f_max_topic)
            self._pub_sub_manager.unsubscribe(self, self._th_PaP_topic)
            self._pub_sub_manager.unsubscribe(self, self._th_Neg_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_tNe_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_tNe_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_tPo_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_tPo_topic)
            self._pub_sub_manager.unsubscribe(self, self._age_criterion_topic)
            self._pub_sub_manager.unsubscribe(self, self._years_topic)
            self._pub_sub_manager.unsubscribe(self, self._months_topic)
            self._pub_sub_manager.unsubscribe(self, self._sex_criterion_topic)
            self._pub_sub_manager.unsubscribe(self, self._sex_topic)
            self._pub_sub_manager.unsubscribe(self, self._det_param_topic)
            self._pub_sub_manager.unsubscribe(self, self._group1_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name1_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group2_topic)   
            self._pub_sub_manager.unsubscribe(self, self._name2_topic)  
            
