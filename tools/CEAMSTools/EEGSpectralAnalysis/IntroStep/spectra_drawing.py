"""
    The example spectra of the introduction of EEG Spectral Power Analysis, drawn by the code: the power
    of an example recording in N2 and in N3, on two channels (Cz-A1 and O1-A2), side by side on the same
    log scale. Painted at the width of its label, in the colors of the theme (light and dark).

    The values are the 1 Hz bands of the recording, read from the vector images of the module PSA Pics
    Generator (cohort_psa_mean_std_Total_<channel>_3x2.pdf, mean of one recording: no standard deviation).
"""
import math

from qtpy import QtCore, QtGui

# Height of the figure (pixels); it takes the width of its card
FIGURE_HEIGHT = 330

# Power of the 1 Hz bands [0-1[, [1-2[ ... [59-60[ Hz at their centers, log10 of uV2/Hz
FREQUENCIES = tuple(band + 0.5 for band in range(60))
LOG_POWER = {
    "Cz-A1": {
        "N2": (
            1.894, 2.056, 1.813, 1.641, 1.443, 1.246, 1.133, 1.111, 1.038, 0.916, 0.771, 0.717, 0.702,
            0.681, 1.022, 0.740, 0.279, 0.088, 0.000, -0.060, -0.144, -0.195, -0.252, -0.341, -0.429,
            -0.488, -0.585, -0.654, -0.701, -0.756, -0.856, -0.959, -1.054, -1.123, -1.210, -1.288, -1.386,
            -1.477, -1.561, -1.670, -1.780, -1.882, -1.986, -2.096, -2.210, -2.325, -2.426, -2.556, -2.766,
            -2.923, -2.832, -2.989, -2.972, -3.029, -3.100, -3.158, -3.185, -3.205, -3.223, -3.238
        ),
        "N3": (
            2.506, 2.583, 2.133, 1.906, 1.639, 1.454, 1.319, 1.215, 1.130, 1.011, 0.860, 0.744, 0.674,
            0.693, 1.038, 0.624, 0.115, -0.067, -0.167, -0.284, -0.357, -0.428, -0.500, -0.559, -0.656,
            -0.703, -0.773, -0.826, -0.854, -0.881, -1.003, -1.099, -1.146, -1.238, -1.345, -1.421, -1.517,
            -1.616, -1.698, -1.782, -1.911, -2.006, -2.120, -2.230, -2.329, -2.418, -2.513, -2.617, -2.793,
            -2.933, -2.834, -3.002, -3.003, -3.065, -3.143, -3.175, -3.218, -3.224, -3.246, -3.250
        ),
    },
    "O1-A2": {
        "N2": (
            1.891, 1.942, 1.591, 1.447, 1.288, 1.186, 1.102, 1.073, 1.037, 0.931, 0.763, 0.628, 0.486,
            0.435, 0.808, 0.544, 0.022, -0.189, -0.334, -0.420, -0.515, -0.581, -0.653, -0.731, -0.804,
            -0.865, -0.920, -0.959, -1.004, -1.056, -1.135, -1.209, -1.312, -1.376, -1.452, -1.532, -1.625,
            -1.720, -1.806, -1.903, -2.008, -2.107, -2.213, -2.321, -2.429, -2.515, -2.595, -2.688, -2.833,
            -2.980, -2.868, -3.091, -3.064, -3.095, -3.143, -3.203, -3.232, -3.240, -3.257, -3.254
        ),
        "N3": (
            2.328, 2.370, 1.889, 1.679, 1.506, 1.420, 1.295, 1.187, 1.071, 0.903, 0.681, 0.499, 0.368,
            0.410, 0.830, 0.441, -0.120, -0.327, -0.452, -0.562, -0.656, -0.736, -0.804, -0.875, -0.947,
            -1.007, -1.074, -1.116, -1.122, -1.162, -1.262, -1.350, -1.403, -1.492, -1.581, -1.648, -1.761,
            -1.849, -1.934, -2.035, -2.137, -2.216, -2.322, -2.423, -2.512, -2.599, -2.681, -2.726, -2.961,
            -3.070, -2.912, -3.042, -3.065, -3.069, -3.147, -3.214, -3.237, -3.255, -3.260, -3.262
        ),
    },
}
STAGES = ("N2", "N3")

# The axes: 0 to 60 Hz (a tick every 10 Hz), 10^-3.5 to 10^3 uV2/Hz (a tick every decade)
F_MAX = 60
F_TICK = 10
LOG_MIN, LOG_MAX = -3.5, 3.0

# One color per stage: the first two colors of a categorical palette checked for color vision
# deficiencies, a step for each theme (on the card: #ffffff light, #1c2431 dark)
STAGE_COLORS = {
    "light": {"N2": "#2a78d6", "N3": "#eb6834"},
    "dark": {"N2": "#3987e5", "N3": "#d95926"},
}
# The lines and texts of the axes, colors of the Snooz themes: the grid in the color of the separators
# (token separator), the axes a step darker (token scrollbar_handle), the texts muted (token text_muted)
AXES_COLORS = {
    "light": {"grid": "#e1e7ef", "axis": "#b5c2d3", "muted": "#5b6b82"},
    "dark": {"grid": "#2a3446", "axis": "#3d4a61", "muted": "#9aa8bd"},
}


def _decade_label(exponent):
    """ The label of a decade: 10 and its exponent, written as a superscript (with a minus sign). """
    return "10", str(exponent).replace("-", "−")


def _place_label(text_size, curves, own, x_of, y_of, plot, above):
    """ The rectangle of the direct label of a curve, near the curve at low frequencies, where the stages
        differ most: above and to the right of it (above), or below and to the left of it, at the first
        frequency where the label stays 4 px away from every curve and inside the plot. None if there is
        none. """
    width, height = text_size.width(), text_size.height()
    # Further frequencies for the narrow figures (small windows): the label must stay inside the plot
    frequencies = (2.5, 3.5, 4.5, 5.5, 6.5, 8.5, 1.5) if above else (3.5, 4.5, 2.5, 5.5, 6.5, 8.5, 10.5, 12.5, 1.5)

    def curve_y(values, x):
        for index in range(len(FREQUENCIES) - 1):
            x1, x2 = x_of(FREQUENCIES[index]), x_of(FREQUENCIES[index + 1])
            if x1 <= x <= x2:
                ratio = (x - x1) / (x2 - x1)
                return y_of(values[index] + ratio * (values[index + 1] - values[index]))
        return None

    for frequency in frequencies:
        x = x_of(frequency)
        y = curve_y(own, x)
        rect = QtCore.QRectF(x + 5, y - 5 - height, width, height) if above else \
            QtCore.QRectF(x - 5 - width, y + 5, width, height)
        if not plot.adjusted(4, 4, -4, -4).contains(rect):
            continue
        clear = True
        step = 1.0
        sample = rect.left() - 4
        while clear and sample <= rect.right() + 4:
            for values in curves:
                value = curve_y(values, sample)
                if value is not None and rect.top() - 4 < value < rect.bottom() + 4:
                    clear = False
            sample += step
        if clear:
            return rect
    return None


def draw_spectra(painter, width, height, palette, font):
    """ Draw the example spectra in a width x height area, in the colors of the theme (palette): a panel
        per channel, the power of N2 and N3 (a color each) on a log scale shared by the panels, the
        legend at the top right and the name of each stage next to its line. """
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing)
    theme = "dark" if palette.color(QtGui.QPalette.ColorRole.Base).lightness() < 128 else "light"
    text = palette.color(QtGui.QPalette.ColorRole.Text)
    colors = {stage: QtGui.QColor(STAGE_COLORS[theme][stage]) for stage in STAGES}
    grid = QtGui.QColor(AXES_COLORS[theme]["grid"])
    axis = QtGui.QColor(AXES_COLORS[theme]["axis"])
    muted = QtGui.QColor(AXES_COLORS[theme]["muted"])

    small = QtGui.QFont(font)
    small.setPixelSize(13)
    small.setBold(False)
    strong = QtGui.QFont(small)
    strong.setWeight(QtGui.QFont.Weight.DemiBold)
    title = QtGui.QFont(font)
    title.setPixelSize(15)
    title.setWeight(QtGui.QFont.Weight.DemiBold)
    superscript = QtGui.QFont(small)
    superscript.setPixelSize(10)
    small_metrics = QtGui.QFontMetricsF(small)
    strong_metrics = QtGui.QFontMetricsF(strong)
    title_metrics = QtGui.QFontMetricsF(title)
    superscript_metrics = QtGui.QFontMetricsF(superscript)
    text_height = small_metrics.height()

    exponents = range(math.ceil(LOG_MIN), math.floor(LOG_MAX) + 1)

    def decade_width(exponent):
        base, power = _decade_label(exponent)
        return small_metrics.horizontalAdvance(base) + 1 + superscript_metrics.horizontalAdvance(power)

    # Vertical: the titles of the panels and the legend, the plots, the frequencies and their title
    plot_top = math.ceil(title_metrics.height()) + 12
    plot_bottom = math.floor(height - 2 * text_height - 12)
    # Horizontal: the title of the power (turned), the decades, the plots
    left = text_height + 10 + max(decade_width(e) for e in exponents) + 8
    right = small_metrics.horizontalAdvance(str(F_MAX)) / 2 + 1
    gap = 44
    plot_width = math.floor((width - left - right - gap) / 2)
    panels = [math.floor(left), math.floor(left) + plot_width + gap]

    def y_of(log_power):
        return plot_bottom - (log_power - LOG_MIN) / (LOG_MAX - LOG_MIN) * (plot_bottom - plot_top)

    def crisp(value):
        return math.floor(value) + 0.5

    center = QtCore.Qt.AlignmentFlag.AlignCenter
    left_center = QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter

    for index, (channel, curves) in enumerate(LOG_POWER.items()):
        panel_left = panels[index]
        plot = QtCore.QRectF(panel_left, plot_top, plot_width, plot_bottom - plot_top)

        def x_of(frequency, panel_left=panel_left):
            return panel_left + frequency / F_MAX * plot_width

        # The grid: a line per decade and per frequency tick, then the axes
        painter.setPen(QtGui.QPen(grid, 1))
        for exponent in exponents:
            y = crisp(y_of(exponent))
            painter.drawLine(QtCore.QPointF(panel_left, y), QtCore.QPointF(panel_left + plot_width, y))
        for frequency in range(F_TICK, F_MAX + 1, F_TICK):
            x = crisp(x_of(frequency))
            painter.drawLine(QtCore.QPointF(x, plot_top), QtCore.QPointF(x, plot_bottom))
        painter.setPen(QtGui.QPen(axis, 1))
        painter.drawLine(QtCore.QPointF(crisp(panel_left), plot_top), QtCore.QPointF(crisp(panel_left), crisp(plot_bottom)))
        painter.drawLine(QtCore.QPointF(panel_left, crisp(plot_bottom)), QtCore.QPointF(panel_left + plot_width, crisp(plot_bottom)))

        # The frequencies under the panel, the decades left of the first panel only (shared scale)
        painter.setFont(small)
        painter.setPen(muted)
        for frequency in range(0, F_MAX + 1, F_TICK):
            x = x_of(frequency)
            painter.drawText(QtCore.QRectF(x - 20, plot_bottom + 5, 40, text_height), center, str(frequency))
        if index == 0:
            # 10 centered on its grid line, its exponent smaller and raised (superscript)
            for exponent in exponents:
                base, power = _decade_label(exponent)
                baseline = y_of(exponent) + small_metrics.capHeight() / 2
                power_x = panel_left - 8 - superscript_metrics.horizontalAdvance(power)
                base_x = power_x - 1 - small_metrics.horizontalAdvance(base)
                painter.setFont(small)
                painter.drawText(QtCore.QPointF(base_x, baseline), base)
                painter.setFont(superscript)
                painter.drawText(QtCore.QPointF(power_x, baseline - 0.55 * small_metrics.capHeight()), power)
            painter.setFont(small)

        # The power of each stage: a 2 px line through the bands
        painter.save()
        painter.setClipRect(plot.adjusted(0, -2, 2, 0))
        for stage in STAGES:
            path = QtGui.QPainterPath()
            for frequency, log_power in zip(FREQUENCIES, curves[stage]):
                point = QtCore.QPointF(x_of(frequency), y_of(log_power))
                if path.elementCount():
                    path.lineTo(point)
                else:
                    path.moveTo(point)
            painter.setPen(QtGui.QPen(colors[stage], 2, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap,
                                      QtCore.Qt.PenJoinStyle.RoundJoin))
            painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
            painter.drawPath(path)
        painter.restore()

        # The name of each stage next to its line: N3 above its line, N2 below its line
        painter.setFont(strong)
        painter.setPen(text)
        for stage in STAGES:
            size = strong_metrics.size(0, stage)
            rect = _place_label(size, [curves[s] for s in STAGES], curves[stage], x_of, y_of, plot,
                                above=stage == "N3")
            if rect is not None:
                painter.drawText(rect, center, stage)

        # The title of the panel: the channel
        painter.setFont(title)
        painter.setPen(text)
        painter.drawText(QtCore.QRectF(panel_left, 0, plot_width, title_metrics.height()), left_center, channel)

    # The legend, at the top right: a line of the color of each stage and its name
    painter.setFont(small)
    key_length, key_gap, item_gap = 18, 6, 16
    items = [(stage, small_metrics.horizontalAdvance(stage)) for stage in STAGES]
    legend_width = sum(key_length + key_gap + advance for _, advance in items) + item_gap * (len(items) - 1)
    x = panels[-1] + plot_width - legend_width
    y = title_metrics.height() / 2
    for stage, advance in items:
        painter.setPen(QtGui.QPen(colors[stage], 2, QtCore.Qt.PenStyle.SolidLine, QtCore.Qt.PenCapStyle.RoundCap))
        painter.drawLine(QtCore.QPointF(x + 1, y), QtCore.QPointF(x + key_length - 1, y))
        painter.setPen(text)
        painter.drawText(QtCore.QRectF(x + key_length + key_gap, y - text_height / 2, advance + 2, text_height),
                         left_center, stage)
        x += key_length + key_gap + advance + item_gap

    # The titles of the axes: the frequency under the panels, the log power (turned) left of the decades
    painter.setFont(small)
    painter.setPen(muted)
    painter.drawText(QtCore.QRectF(panels[0], plot_bottom + 5 + text_height + 4, panels[-1] + plot_width - panels[0],
                                   text_height), center, "Frequency (Hz)")
    painter.save()
    painter.translate(0, (plot_top + plot_bottom) / 2)
    painter.rotate(-90)
    painter.drawText(QtCore.QRectF(-(plot_bottom - plot_top) / 2, 0, plot_bottom - plot_top, text_height), center,
                     "Log power (µV²/Hz)")
    painter.restore()


class SpectraDrawing(QtCore.QObject):
    """ Paints the example spectra on its label, at the width of the label, when the label is painted:
        sharp on every screen and in the colors of the theme. The label has no picture, so the page does
        not put it in a picture card (made for pictures on a white background).
    """
    def __init__(self, label):
        super().__init__(label)
        label.setMinimumHeight(FIGURE_HEIGHT)
        label.setMaximumHeight(FIGURE_HEIGHT)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_spectra(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)
