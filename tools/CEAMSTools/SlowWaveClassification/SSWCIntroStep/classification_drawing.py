"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Illustration of the classification of Classify Slow Waves, drawn by the code: the histogram of the transition
    frequencies of the slow waves of a cohort with the Gaussian mixture fitted to it, as in the picture that the
    module Slow Wave Classifier saves in the output folder, and the bars colored by category. The data are those of
    the picture shown by the tool before (transition_frequency.png): the count of each of its 100 bars and its
    mixture of three components. The categories come from a k-means started from the means of the components, as in
    the module. Painted on a label at its width and in the colors of the theme (as the drawings of Detect EEG
    Artifacts).
"""
import numpy as np
from qtpy import QtCore, QtGui

HEIGHT = 240

# The histogram: 100 bins from the lowest to the highest transition frequency (Hz), the count of slow waves per bin
RANGE = (0.283, 3.046)
COUNTS = (1, 2, 3, 6, 6, 13, 14, 20, 24, 27, 40, 47, 45, 34, 42, 45, 45, 55, 41, 30,
          43, 54, 40, 56, 59, 52, 55, 49, 60, 45, 40, 32, 35, 27, 34, 31, 25, 23, 15, 20,
          5, 21, 21, 12, 19, 3, 22, 8, 13, 17, 3, 9, 23, 24, 13, 13, 10, 17, 19, 22,
          12, 0, 19, 14, 24, 26, 20, 0, 16, 11, 14, 0, 10, 9, 0, 9, 0, 10, 6, 0,
          4, 0, 2, 0, 3, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2)
# The Gaussian mixture fitted to the transition frequencies, as (weight, mean, standard deviation) in Hz
COMPONENTS = ((0.186, 0.620, 0.117), (0.522, 0.999, 0.210), (0.292, 1.862, 0.363))
X_TICKS = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
Y_TICKS = (0, 20, 40, 60)

TITLE = "Distribution of the transition frequency of sleep slow waves"
X_TITLE = "Transition frequency (Hz)"
Y_TITLE = "Number of slow waves"


def classification_data():
    """ The bin edges, the count of slow waves per bin, the category of each bin (1 to 3), and the Gaussian mixture
        on a fine grid (x, y).
        The categories: a k-means of the transition frequencies (the middle of each bin, weighted by its count)
        started from the means of the components, as in the module Slow Wave Classifier; category 1 has the slowest
        transitions.
        The mixture is scaled as in the picture of the module (number of slow waves / 25). """
    edges = np.linspace(RANGE[0], RANGE[1], len(COUNTS) + 1)
    counts = np.array(COUNTS)
    middles = (edges[:-1] + edges[1:]) / 2
    centers = np.array([mean for _, mean, _ in COMPONENTS])
    for _ in range(50):
        labels = np.argmin(np.abs(middles[:, None] - centers[None, :]), axis=1)
        new_centers = np.array([np.average(middles[labels == k], weights=counts[labels == k])
                                for k in range(len(centers))])
        if np.allclose(new_centers, centers):
            break
        centers = new_centers
    categories = np.argsort(np.argsort(centers))[labels] + 1
    grid = np.arange(RANGE[0], RANGE[1], 0.005)
    density = sum(weight * np.exp(-0.5 * ((grid - mean) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))
                  for weight, mean, sd in COMPONENTS)
    return edges, counts, categories, grid, density * counts.sum() / 25


def drawing_colors(palette):
    """ The colors of the categories (the link color of the theme, a green and a purple) and of the mixture (an
        orange, as in the picture of the module), chosen to read on light and dark backgrounds. """
    link = palette.color(QtGui.QPalette.ColorRole.Link)
    dark = palette.color(QtGui.QPalette.ColorRole.Base).lightness() < 128
    categories = [link, QtGui.QColor("#34c26b" if dark else "#16a34a"), QtGui.QColor("#a78bfa" if dark else "#7c3aed")]
    return categories, QtGui.QColor("#f0a040" if dark else "#d9730d")


def draw_classification(painter, width, height, palette, font):
    """ Draw the histogram in a width x height area: the title, the bars in the color of their category, the
        Gaussian mixture over them, both axes with their ticks and titles, and the legend at the top right of the
        plot. """
    edges, counts, categories, grid, mixture = classification_data()
    small = QtGui.QFont(font)
    small.setPixelSize(13)
    big = QtGui.QFont(font)
    big.setPixelSize(14)
    metrics = QtGui.QFontMetrics(small)
    line_height = metrics.height()

    text = palette.color(QtGui.QPalette.ColorRole.Text)
    muted = QtGui.QColor(text)
    muted.setAlpha(150)
    category_colors, mixture_color = drawing_colors(palette)
    for color in category_colors:
        color.setAlpha(170)

    # The plot area: the y-axis title and tick labels on the left, the x-axis tick labels and title below
    tick_width = max(metrics.horizontalAdvance(str(tick)) for tick in Y_TICKS)
    left = line_height + 8.0 + tick_width + 8.0
    right = width - 6.0
    top = QtGui.QFontMetrics(big).height() + 10.0
    bottom = height - 2 * line_height - 8.0
    span = RANGE[1] - RANGE[0]
    x_min, x_max = RANGE[0] - 0.05 * span, RANGE[1] + 0.05 * span
    y_max = max(counts.max(), mixture.max()) * 1.05

    def to_x(value):
        return left + (value - x_min) / (x_max - x_min) * (right - left)

    def to_y(value):
        return bottom - value / y_max * (bottom - top)

    # The title
    painter.setFont(big)
    painter.setPen(QtGui.QPen(text))
    painter.drawText(QtCore.QRectF(left, 0, right - left, top - 6), QtCore.Qt.AlignmentFlag.AlignCenter, TITLE)
    painter.setFont(small)

    # The bars, side by side, in the color of their category (without antialiasing: no seam between two bars)
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    for index, count in enumerate(counts):
        if count:
            painter.setBrush(category_colors[categories[index] - 1])
            x0, x1 = round(to_x(edges[index])), round(to_x(edges[index + 1]))
            painter.drawRect(QtCore.QRectF(x0, to_y(count), x1 - x0, bottom - to_y(count)))

    # The Gaussian mixture over the bars
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    curve = QtGui.QPainterPath(QtCore.QPointF(to_x(grid[0]), to_y(mixture[0])))
    for value, count in zip(grid[1:], mixture[1:]):
        curve.lineTo(to_x(value), to_y(count))
    painter.setPen(QtGui.QPen(mixture_color, 2.0))
    painter.drawPath(curve)

    # The x axis: line, ticks, tick labels and title
    painter.setPen(QtGui.QPen(muted, 1.0))
    painter.drawLine(QtCore.QPointF(left, bottom), QtCore.QPointF(right, bottom))
    for tick in X_TICKS:
        x = to_x(tick)
        painter.drawLine(QtCore.QPointF(x, bottom), QtCore.QPointF(x, bottom + 4))
        painter.drawText(QtCore.QRectF(x - 30, bottom + 5, 60, line_height), QtCore.Qt.AlignmentFlag.AlignCenter,
                         f"{tick:.1f}")
    painter.drawText(QtCore.QRectF(left, height - line_height - 1, right - left, line_height),
                     QtCore.Qt.AlignmentFlag.AlignCenter, X_TITLE)

    # The y axis: line, ticks, tick labels and title (turned)
    painter.drawLine(QtCore.QPointF(left, top), QtCore.QPointF(left, bottom))
    for tick in Y_TICKS:
        y = to_y(tick)
        painter.drawLine(QtCore.QPointF(left - 4, y), QtCore.QPointF(left, y))
        painter.drawText(QtCore.QRectF(left - 6 - tick_width - 2, y - line_height / 2, tick_width + 2, line_height),
                         QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter, str(tick))
    painter.save()
    painter.translate(0, (top + bottom) / 2)
    painter.rotate(-90)
    painter.drawText(QtCore.QRectF(-(bottom - top) / 2, 0, bottom - top, line_height),
                     QtCore.Qt.AlignmentFlag.AlignCenter, Y_TITLE)
    painter.restore()

    # The legend at the top right of the plot: the bars of each category, then the mixture
    items = [(f"Category {index + 1}", color, "box") for index, color in enumerate(category_colors)]
    items.append(("Gaussian mixture", mixture_color, "line"))
    y = top + 4
    name_width = max(metrics.horizontalAdvance(name) for name, _, _ in items)
    x = right - 4 - name_width
    for name, color, kind in items:
        mark_y = y + line_height / 2
        if kind == "box":
            painter.setPen(QtCore.Qt.PenStyle.NoPen)
            painter.setBrush(color)
            painter.drawRect(QtCore.QRectF(x - 22, mark_y - 6, 14, 12))
            painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
        else:
            painter.setPen(QtGui.QPen(color, 2.0))
            painter.drawLine(QtCore.QPointF(x - 24, mark_y), QtCore.QPointF(x - 6, mark_y))
        painter.setPen(QtGui.QPen(text))
        painter.drawText(QtCore.QRectF(x, y, name_width + 2, line_height),
                         QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, name)
        y += line_height + 4


class ClassificationDrawing(QtCore.QObject):
    """ Paints the illustration of the classification on its label, at the width of the label, when the label is
        painted: sharp on every screen and in the colors of the theme. The label has no picture. """
    def __init__(self, label, height=HEIGHT):
        super().__init__(label)
        label.setPixmap(QtGui.QPixmap())
        label.setMinimumHeight(height)
        label.setMaximumHeight(height)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_classification(painter, label.width(), label.height(), label.palette(), label.font())
            painter.end()
            return True
        return super().eventFilter(label, event)
