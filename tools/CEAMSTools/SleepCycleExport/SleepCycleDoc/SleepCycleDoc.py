"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    SleepCycleDoc
    Step of the Tool Description
"""
from qtpy import QtCore, QtGui, QtWidgets

from CEAMSTools.SleepCycleExport.SleepCycleDoc.Ui_SleepCycleDoc import Ui_SleepCycleDoc
from commons.BaseStepView import BaseStepView

# Height of the illustration of the sleep cycles (pixels); it takes the width of its card
IMAGE_HEIGHT = 220
# The sleep stages of the example, one character per 30 s epoch: the first 9 hours of learn-nsrr01
# (public NSRR recording; it ends awake). W: wake, 1, 2, 3: N1, N2, N3, R: REM.
STAGES = (
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW111W111WW11W11WWWW11WWW111111W1112222"
    "22222222222222222222222222222222222222222222222222222222222222W12222222W11RWW11R1WRRRR111W"
    "WW12W12222222222222222222222W2222222222222222222222222222223222232222222222222222222223WW1"
    "12222222222222222222222222222222222222222RRRRRWRRWWW22WRRR1RWR1RRRW1R1RRRWRRRWRWWRRRRRRRRR"
    "RRRRRRRR1RRRWRRRRRRRWRRR2222222111222WWWWWWWWWWWWWWWWWWWWWWWWWWWWW1111WWWW111WWWWWWWW11WW1"
    "222222222222222222222222222222222W11222223222222222222222222222222222222222222222222222222"
    "2223WWWWWWWWWWWW1W11111111111WWWWWWW11122222222RRRRRRWRRRRRRRWRRWRRRRRRRRRRRRRRRWRRRRRRWRR"
    "RRRRRRRRRRRRRRRRWRRRRRR2222222222222222222222222222222212222222222222222222222222222222W11"
    "11222222222222222222223222222322222222222222RRRRRRRRRRRRRRRRRRRRRWRRRRRRRRRRRRRRRRRRRRRRWW"
    "WWWW11112222222222222222222222222222222222222222222222RR22222222222222222222222RRRRRRRRRRR"
    "RWRRRRRRRRRRRRRRRRRRRRRRRRRRRRWRRRRRRRWWWW111111111111122222222222222222222222222222222222"
    "2222222222W1111122223333333333RWWRRWWRRWRRRWRRRRRRWRRRRRWRRRRRRRRWWW111W111111111122WWWWWW"
)
EPOCHS_PER_HOUR = 120
# Its sleep cycles, given by the module Sleep Cycles Delimiter (minimum criteria): the first and last
# epochs (inclusive) of the NREM period and of the REM period of each cycle
CYCLES = [((53, 163), (164, 175)), ((176, 310), (311, 383)), ((384, 586), (587, 652)),
          ((653, 763), (764, 807)), ((814, 863), (864, 937)), ((942, 1019), (1020, 1054))]
# The incomplete cycle at the end of the night: a NREM period without a REM period
INCOMPLETE = (1058, 1073)
# The rows of the hypnogram, from top to bottom: their name and their stage in STAGES
LEVELS = [("Wake", "W"), ("REM", "R"), ("N1", "1"), ("N2", "2"), ("N3", "3")]
# Color of the REM periods and stages: the green of the light and dark themes (success)
REM_COLORS = {"light": "#16a34a", "dark": "#34c26b"}


def draw_sleep_cycles(painter, width, height, palette, font):
    """ Draw the hypnogram of the example and its sleep cycles in a width x height area, in the colors
        of the theme (palette): on top, the cycles C1 to C6, each a bar of its NREM period (link color)
        then of its REM period (green), and the incomplete cycle in gray; below, the hypnogram in the
        text color on light bands of the periods, its R stages in green, and the time in hours.
    """
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    metrics = QtGui.QFontMetrics(small)
    text_height = metrics.height()

    def tint(color, alpha):
        tinted = QtGui.QColor(color)
        tinted.setAlpha(alpha)
        return tinted

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = tint(text, 150)
    dark = palette.color(QtGui.QPalette.ColorRole.Base).lightness() < 128
    nrem = palette.color(QtGui.QPalette.ColorRole.Link)
    rem = QtGui.QColor(REM_COLORS["dark" if dark else "light"])

    last_hour = len(STAGES) // EPOCHS_PER_HOUR
    left = max(metrics.horizontalAdvance(name) for name, _ in LEVELS) + 12.0
    right = width - metrics.horizontalAdvance(f"{last_hour} h") / 2 - 2
    bar_top = text_height + 2.0
    bar_height = 12.0
    top = bar_top + bar_height + 10
    bottom = height - text_height - 8
    row = (bottom - top) / len(LEVELS)
    level_y = {stage: top + row * (index + 0.5) for index, (_, stage) in enumerate(LEVELS)}

    def x_of(epoch):
        return left + epoch / len(STAGES) * (right - left)

    center = QtCore.Qt.AlignmentFlag.AlignCenter
    left_center = QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter

    # The rows of the stages: a light line and the name of the stage
    for name, stage in LEVELS:
        painter.setPen(QtGui.QPen(tint(text, 28), 1))
        painter.drawLine(QtCore.QPointF(left, level_y[stage]), QtCore.QPointF(right, level_y[stage]))
        painter.setPen(muted)
        painter.drawText(QtCore.QRectF(0, level_y[stage] - text_height / 2, left - 6, text_height), left_center, name)

    # The cycles: a light band of each period across the hypnogram, the bars of the periods and the
    # number of the cycle above them (a gap of 2 px between two cycles)
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    for number, periods in enumerate(CYCLES, 1):
        for (first, last), color in zip(periods, (nrem, rem)):
            x1, x2 = x_of(first), x_of(last + 1)
            painter.fillRect(QtCore.QRectF(x1, top, x2 - x1, bottom - top), tint(color, 26))
            bar_x1 = x1 + 1 if color is nrem else x1
            bar_x2 = x2 - 1 if color is rem else x2
            painter.fillRect(QtCore.QRectF(bar_x1, bar_top, bar_x2 - bar_x1, bar_height), tint(color, 210))
        x1, x2 = x_of(periods[0][0]), x_of(periods[1][1] + 1)
        painter.setPen(text)
        painter.drawText(QtCore.QRectF(x1, 0, x2 - x1, text_height), center, f"C{number}")
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
    x1, x2 = x_of(INCOMPLETE[0]), x_of(INCOMPLETE[1] + 1)
    painter.fillRect(QtCore.QRectF(x1 + 1, bar_top, x2 - x1 - 2, bar_height), tint(text, 90))

    # The hypnogram: one step per epoch, then the R stages in green on top
    trace = QtGui.QPainterPath(QtCore.QPointF(x_of(0), level_y[STAGES[0]]))
    for epoch, stage in enumerate(STAGES):
        trace.lineTo(x_of(epoch), level_y[stage])
        trace.lineTo(x_of(epoch + 1), level_y[stage])
    painter.setPen(QtGui.QPen(tint(text, 220), 1.1))
    painter.drawPath(trace)
    painter.setPen(QtGui.QPen(rem, 3.5, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.FlatCap))
    epoch = 0
    while epoch < len(STAGES):
        if STAGES[epoch] == "R":
            end = epoch
            while end + 1 < len(STAGES) and STAGES[end + 1] == "R":
                end += 1
            painter.drawLine(QtCore.QPointF(x_of(epoch), level_y["R"]), QtCore.QPointF(x_of(end + 1), level_y["R"]))
            epoch = end
        epoch += 1

    # The time from the start of the recording, in hours
    for hour in range(last_hour + 1):
        x = x_of(hour * EPOCHS_PER_HOUR)
        painter.setPen(QtGui.QPen(muted, 1))
        painter.drawLine(QtCore.QPointF(x, bottom), QtCore.QPointF(x, bottom + 4))
        painter.drawText(QtCore.QRectF(x - 30, bottom + 6, 60, text_height), center, f"{hour} h")


class SleepCyclesDrawing(QtCore.QObject):
    """ Paints the hypnogram of the example and its sleep cycles on its label, at the width of the label,
        when the label is painted: sharp on every screen and in the colors of the theme. The label has no
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
            draw_sleep_cycles(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)


class SleepCycleDoc( BaseStepView,  Ui_SleepCycleDoc, QtWidgets.QWidget):
    """
        SleepCycleDoc
        Step of the Tool Description
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # The hypnogram of the example and its sleep cycles, painted on hypnogram_pic
        self._cycles_drawing = SleepCyclesDrawing(self.hypnogram_pic)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
