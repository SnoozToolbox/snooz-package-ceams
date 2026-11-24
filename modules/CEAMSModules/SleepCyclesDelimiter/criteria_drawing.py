"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    The illustration of the period duration criteria of the sleep cycles (settings view of
    SleepCyclesDelimiter), drawn by the code: sharp on every screen and in the colors of the theme.
    Each cycle is a block of its NREM and REM periods with their minimum durations, a bracket of the
    color of the cycle under it and, on the right, the stages of the NREM periods and when a cycle is
    complete.
"""
from qtpy import QtCore, QtGui

# Height of the illustration (pixels), with a margin of 10 px above; it takes the width of its label
IMAGE_HEIGHT = 140

# Colors of the brackets of the cycles (same in the light and dark themes)
FIRST = "#ff9966"       # orange
MIDDLE = "#ffc000"      # gold
LAST = "#92d050"        # light green
VALIDATE = "#00b050"    # green
# The REM periods: blue, lighter in the dark theme (the NREM periods: gray, a tint of the text color)
REMP_COLORS = {"light": "#2e75b6", "dark": "#5b9bd5"}

_INCOMPLETE = "A cycle is incomplete if its NREMP or its REMP does not meet the minimum duration."
_DURATIONS = [("NREMP", "≥ 15 min"), ("REMP", "> 0 min"), ("NREMP", "≥ 15 min"), ("REMP", "≥ 5 min"),
              ("NREMP", "≥ 15 min")]

# The criteria: the periods (name, minimum duration), the cycles (first and last period, label,
# color of the bracket), the stages of the NREM periods and the rule of a complete cycle.
CRITERIA = {
    "minimal": {
        "periods": [("NREMP", "> 0 min"), ("REMP", "> 0 min")] * 3,
        "cycles": [(0, 1, "First\ncycle", FIRST), (2, 3, "Middle\ncycles", MIDDLE), (4, 5, "Last\ncycle", LAST)],
        "stages": "N1, N2, N3 (stage 4)",
        # no-break spaces: "(> 0 min)" stays on one line
        "rule": "No duration criteria. A cycle is complete if it has a NREMP (> 0 min) and a REMP "
                "(> 0 min).",
    },
    "aeschbach": {
        "periods": _DURATIONS + [("REMP", "> 0 min"), ("NREMP", "≥ 5 min")],
        "cycles": [(0, 1, "First\ncycle", FIRST), (2, 3, "Middle\ncycles", MIDDLE),
                   (4, 5, "Last complete\ncycle", LAST), (6, 6, "To validate\nlast cycle", VALIDATE)],
        "stages": "N2, N3 (stage 4)",
        "rule": _INCOMPLETE,
    },
    "feinberg_floyd": {
        "periods": _DURATIONS + [("REMP", "≥ 5 min"), ("NREMP", "≥ 5 min")],
        "cycles": [(0, 1, "First\ncycle", FIRST), (2, 3, "Middle\ncycles", MIDDLE),
                   (4, 5, "Last complete\ncycle", LAST), (6, 6, "To validate\nlast cycle", VALIDATE)],
        "stages": "N2, N3 (stage 4)",
        "rule": _INCOMPLETE,
    },
}


def draw_criteria(painter, width, height, palette, font, criteria):
    """ Draw the illustration of the criteria (a key of CRITERIA) in a width x height area, in the
        colors of the theme (palette): each cycle is one rounded block, its NREM period (gray) then its
        REM period (blue), with their minimum durations; a small gap separates two cycles. A bracket of
        the color of the cycle and its label are under each block; the stages of the NREM periods and
        the rule of a complete cycle are on the right.
    """
    spec = CRITERIA[criteria]
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

    def sized(pixels, weight=QtGui.QFont.Weight.Normal):
        sized_font = QtGui.QFont(font)
        sized_font.setPixelSize(pixels)
        sized_font.setWeight(weight)
        return sized_font

    name_font, duration_font = sized(12, QtGui.QFont.Weight.DemiBold), sized(14, QtGui.QFont.Weight.Medium)
    text_font, title_font = sized(13), sized(13, QtGui.QFont.Weight.DemiBold)
    line_height = QtGui.QFontMetrics(text_font).height()

    def tint(color, alpha):
        tinted = QtGui.QColor(color)
        tinted.setAlpha(alpha)
        return tinted

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    dark = palette.color(QtGui.QPalette.ColorRole.Base).lightness() < 128
    blue = QtGui.QColor(REMP_COLORS["dark" if dark else "light"])
    fills = {"NREMP": tint(text, 26 if dark else 20), "REMP": tint(blue, 80 if dark else 60)}
    # The name of a period: the text color for NREMP, blue for REMP
    name_colors = {"NREMP": tint(text, 200), "REMP": blue.lighter(125) if dark else blue.darker(115)}
    outline = QtGui.QPen(tint(text, 150), 1.4)
    separator = QtGui.QPen(tint(text, 90), 1.0)
    center = QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop

    # Geometry: the periods side by side (at most 80 px each), a gap between two cycles, the text on
    # the right (at least 170 px)
    periods, cycles = spec["periods"], spec["cycles"]
    gap, left = 8.0, 1.0
    starts = {first for first, *_ in cycles[1:]}
    period_width = min(80.0, (width - left - 170 - 24 - gap * len(starts)) / len(periods))
    offsets, x = [], left
    for index in range(len(periods)):
        x += gap if index in starts else 0
        offsets.append(x)
        x += period_width
    top, block_height = 10.0, 56.0

    # The cycles: one rounded block each, its periods filled (clipped to the block), a line between
    # two periods, one outline around the block
    for first, last, label, color in cycles:
        block = QtCore.QRectF(offsets[first], top, offsets[last] + period_width - offsets[first], block_height)
        shape = QtGui.QPainterPath()
        shape.addRoundedRect(block, 7, 7)
        painter.save()
        painter.setClipPath(shape)
        for index in range(first, last + 1):
            name = periods[index][0]
            painter.fillRect(QtCore.QRectF(offsets[index], top, period_width, block_height), fills[name])
        painter.restore()
        painter.setPen(separator)
        for index in range(first + 1, last + 1):
            painter.drawLine(QtCore.QPointF(offsets[index], top + 1), QtCore.QPointF(offsets[index], top + block_height - 1))
        painter.setPen(outline)
        painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
        painter.drawPath(shape)
        for index in range(first, last + 1):
            name, duration = periods[index]
            cell = QtCore.QRectF(offsets[index], top, period_width, block_height)
            painter.setPen(name_colors[name])
            painter.setFont(name_font)
            painter.drawText(QtCore.QRectF(cell.left(), cell.top() + 9, cell.width(), line_height), center, name)
            painter.setPen(text)
            painter.setFont(duration_font)
            painter.drawText(QtCore.QRectF(cell.left(), cell.bottom() - 9 - line_height, cell.width(), line_height),
                             center, duration)

        # The bracket of the cycle, in its color, and its label
        x1, x2 = block.left() + 4, block.right() - 4
        middle = (x1 + x2) / 2
        y = block.bottom() + 11
        pen = QtGui.QPen(QtGui.QColor(color), 2.0)
        pen.setCapStyle(QtCore.Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(QtCore.Qt.PenJoinStyle.RoundJoin)
        bracket = QtGui.QPainterPath(QtCore.QPointF(x1, y - 5))
        bracket.lineTo(x1, y)
        bracket.lineTo(x2, y)
        bracket.lineTo(x2, y - 5)
        bracket.moveTo(middle, y)
        bracket.lineTo(middle, y + 5)
        painter.setPen(pen)
        painter.drawPath(bracket)
        painter.setPen(text)
        painter.setFont(text_font)
        painter.drawText(QtCore.QRectF(middle - 60, y + 8, 120, line_height * 2), center, label)

    # On the right: the stages of the NREM periods and when a cycle is complete
    text_left = offsets[-1] + period_width + 24
    text_width = min(260.0, width - text_left)
    flags = QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.TextFlag.TextWordWrap
    painter.setPen(text)
    painter.setFont(title_font)
    painter.drawText(QtCore.QRectF(text_left, top - 2, text_width, line_height), flags, "NREMP stages")
    painter.setFont(text_font)
    painter.drawText(QtCore.QRectF(text_left, top - 2 + line_height, text_width, line_height), flags, spec["stages"])
    painter.drawText(QtCore.QRectF(text_left, top - 2 + line_height * 2.6, text_width, height), flags, spec["rule"])


class CriteriaDrawing(QtCore.QObject):
    """ Paints the illustration of the selected criteria on its label, at the width of the label, when
        the label is painted. The label has no picture, so the page does not put it in a picture card
        (made for pictures on a white background).
    """
    def __init__(self, label, criteria="aeschbach"):
        super().__init__(label)
        self._label = label
        self._criteria = criteria
        label.setMinimumHeight(IMAGE_HEIGHT)
        label.setMaximumHeight(IMAGE_HEIGHT)
        label.installEventFilter(self)

    def set_criteria(self, criteria):
        """ Show the illustration of other criteria (a key of CRITERIA). """
        if criteria in CRITERIA and criteria != self._criteria:
            self._criteria = criteria
            self._label.update()

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_criteria(painter, label.width(), label.height(), label.palette(), label.font(), self._criteria)
            painter.end()
            return True
        return super().eventFilter(label, event)
