# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnalyzeEEGComplexityDoc.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_AnalyzeEEGComplexityDoc(object):
    def setupUi(self, AnalyzeEEGComplexityDoc):
        if not AnalyzeEEGComplexityDoc.objectName():
            AnalyzeEEGComplexityDoc.setObjectName(u"AnalyzeEEGComplexityDoc")
        AnalyzeEEGComplexityDoc.resize(730, 590)
        AnalyzeEEGComplexityDoc.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(AnalyzeEEGComplexityDoc)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AnalyzeEEGComplexityDoc)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(AnalyzeEEGComplexityDoc)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(AnalyzeEEGComplexityDoc)

        QMetaObject.connectSlotsByName(AnalyzeEEGComplexityDoc)
    # setupUi

    def retranslateUi(self, AnalyzeEEGComplexityDoc):
        AnalyzeEEGComplexityDoc.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("AnalyzeEEGComplexityDoc", u"<html><head/><body><p><span style=\" font-weight:700;\">Analyze EEG Complexity</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("AnalyzeEEGComplexityDoc", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Joint Lempel\u2013Ziv complexity (joint)</span>\u00a0quantifies the compressibility of multichannel EEG by treating all selected channels together at each time point (Zozor et al., 2005). Lower values indicate more stereotyped/compressible dynamics; values near 1 after surrogate normalization indicate little structure beyond the power spectrum.</p>\n"
"<p style=\" ma"
                        "rgin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Concatenated Lempel\u2013Ziv complexity (concat)</span>\u00a0first concatenates channels into a single binary sequence (Schartner et al., 2015), then computes Lempel\u2013Ziv complexity on that longer string.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Univariate Lempel\u2013Ziv complexity (univariate)</span>\u00a0computes a normalized complexity for each channel and summarizes across channels (median per epoch), following the approach used by Toker et al. (2022). This mode is recommended for high-density EEG montages.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool computes Fourier-surrogate\u2013normalized Lempel\u2013Ziv complexity (FJZC) as described by To"
                        "ker et al. (2022), based on Lempel\u2013Ziv complexity (Lempel &amp; Ziv, 1976; Kaspar &amp; Schuster, 1987), joint multivariate LZC (Zozor et al., 2005), and concatenated multivariate LZC (Schartner et al., 2015). Signals are binarized from the Hilbert amplitude envelope and normalized against phase-randomized Fourier transform (FT) surrogates (Lancaster et al., 2018).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Important note:<br />Joint mode with a large number of channels (high-density EEG) can produce normalized values close to 1 because the joint state space becomes very large relative to the epoch length. For dense montages, prefer\u00a0univariate. Concat mode is computationally intensive on high-density data.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 - Input Files:<br />Add your PSG files (.edf, .sts or .eeg).<br />The .tsv fil"
                        "e is also needed for the edf format.<br />The .sig file is also needed for the Stellate format.<br />The whole NATUS subject folder is also needed for the NATUS format.<br />Select the montage and the EEG channels to include in the analysis.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - Events Exclusion:<br />Select events to discard from the analysis (i.e. artefacts previously detected and saved in the accessory file).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Important note:<br />Complexity analysis should be performed on brain EEG channels. Any channels marked with the annotation group &quot;art_inspector&quot; and the name &quot;art_channel&quot; or &quot;non_brain&quot; will be automatically excluded from the analysis when that exclusion is configured in the process.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 - Annotation Selection:<br />Choose the recording scope for the analysis:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sleep Stages\u00a0to analyze specific stages</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Unscored\u00a0to analyze the full recording or a chosen time segment</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Specific Annotations\u00a0to base the analysis on event markers</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the analysis is performed on specific annotations, select"
                        " them in this step.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4 - Complexity Settings:<br />Define the complexity mode (joint,\u00a0concat, or\u00a0univariate; default: joint).<br />Specify the epoch length and epoch overlap (in seconds).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">note:<br />Epochs that contain rejected artefacts (NaN/Inf) or are entirely flat/zero are excluded before complexity is computed.<br />Concat mode can be substantially slower than joint or univariate on high-density EEG.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">References:<br />[1] Lempel, A., &amp; Ziv, J. (1976). On the complexity of finite sequences. IEEE Transactions on Information Theory, 22(1), 75\u201381.\u00a0<a href=\"https://doi.org/10.1109/TIT.1976.1055501\"><s"
                        "pan style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1109/TIT.1976.1055501</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[2] Kaspar, F., &amp; Schuster, H. G. (1987). Easily calculable measure for the complexity of spatiotemporal patterns. Physical Review A, 36(2), 842\u2013848.\u00a0<a href=\"https://doi.org/10.1103/PhysRevA.36.842\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1103/PhysRevA.36.842</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[3] Zozor, S., Ravier, P., &amp; Buttelli, O. (2005). On Lempel\u2013Ziv complexity for multidimensional data analysis. Physica A, 345(1\u20132), 285\u2013302.\u00a0<a href=\"https://doi.org/10.1016/j.physa.2004.07.024\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1016/j.physa.2004.07.024</"
                        "span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[4] Schartner, M., Seth, A., Noirhomme, Q., Boly, M., Bruno, M.-A., Laureys, S., &amp; Barrett, A. (2015). Complexity of multi-dimensional spontaneous EEG decreases during propofol-induced general anaesthesia. PLoS ONE, 10(8), e0133532.\u00a0<a href=\"https://doi.org/10.1371/journal.pone.0133532\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1371/journal.pone.0133532</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[5] Toker, D., Pappas, I., Lendner, J. D., Frohlich, J., Mateos, D. M., Mofakham, S., \u2026 &amp; Monti, M. M. (2022). Consciousness is supported by near-critical slow cortical electrodynamics. Proceedings of the National Academy of Sciences, 119(7), e2024455119.\u00a0<a href=\"https://doi.org/10.1073/pnas.2024455119\"><span style=\" t"
                        "ext-decoration: underline; color:#003e92;\">https://doi.org/10.1073/pnas.2024455119</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[6] Lancaster, G., Iatsenko, D., Pidde, A., Ticcinelli, V., &amp; Stefanovska, A. (2018). Surrogate data for hypothesis testing of physical systems. Physics Reports, 748, 1\u201360.\u00a0<a href=\"https://doi.org/10.1016/j.physrep.2018.06.001\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1016/j.physrep.2018.06.001</span></a></p></body></html>", None))
    # retranslateUi

