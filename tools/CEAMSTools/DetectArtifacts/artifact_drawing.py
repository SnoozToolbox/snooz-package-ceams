"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Illustrations of the artifacts of Detect EEG Artifacts, drawn by the code: a simulated EEG with one
    simulated artifact, painted on a label at its width and in the colors of the theme (as the spindle
    of Detect Spindles with A7). Used by the introduction and by the settings page of each detector.
"""
import numpy as np
from qtpy import QtCore, QtGui

# Height of an illustration (pixels): on the introduction (small, without the name: the page writes it next to the
# drawing) and on the page of a detector
SMALL_HEIGHT = 64
LARGE_HEIGHT = 112


def _eeg(time, rng):
    """ A simulated EEG: mixed frequencies, mostly 1-10 Hz (amplitudes in 1/f), unit standard deviation. """
    signal = np.zeros_like(time)
    for frequency in np.linspace(0.7, 10.0, 45):
        signal += rng.normal() / frequency * np.sin(2 * np.pi * frequency * time + rng.uniform(0, 2 * np.pi))
    noise = np.convolve(rng.normal(size=time.size), np.ones(3) / 3, mode="same")
    signal = signal / signal.std() + 0.12 * noise
    return signal / signal.std()


def _band_noise(size, fs, low, high, rng):
    """ White noise kept between low and high Hz (FFT mask), unit standard deviation. """
    spectrum = np.fft.rfft(rng.normal(size=size))
    frequencies = np.fft.rfftfreq(size, 1 / fs)
    spectrum[(frequencies < low) | (frequencies > high)] = 0
    noise = np.fft.irfft(spectrum, size)
    return noise / noise.std()


def _window(time, start, end, ramp):
    """ 1 between start and end, with cosine ramps of ramp seconds at both ends. """
    up = np.clip((time - start) / ramp, 0, 1)
    down = np.clip((end - time) / ramp, 0, 1)
    return np.sin(np.pi / 2 * np.minimum(up, down)) ** 2


def simulated_artifact(kind):
    """ The time (s), the signal and the segments [(start, end)] of the artifact of a detector.
        kind: flatline, high_frequency_burst, persistent_noise, power_line, baseline_variation, muscle.
    """
    rng = np.random.default_rng({"flatline": 3, "high_frequency_burst": 5, "persistent_noise": 7,
                                 "power_line": 9, "baseline_variation": 13, "muscle": 17}[kind])
    if kind == "flatline":
        # The electrode loses contact: the signal is nearly flat
        fs, seconds, segments = 256, 8.0, [(3.2, 5.6)]
        time = np.arange(int(seconds * fs)) / fs
        signal = _eeg(time, rng)
        flat = _window(time, *segments[0], ramp=0.05)
        signal = signal * (1 - flat) + flat * 0.03 * _band_noise(time.size, fs, 1, 40, rng)
    elif kind == "high_frequency_burst":
        # A short burst of high-frequency power (above 25 Hz)
        fs, seconds, segments = 512, 6.0, [(2.8, 3.3)]
        time = np.arange(int(seconds * fs)) / fs
        signal = _eeg(time, rng) + 1.5 * _window(time, *segments[0], ramp=0.05) * \
            _band_noise(time.size, fs, 30, 120, rng)
    elif kind == "persistent_noise":
        # High-frequency noise (above 25 Hz) that lasts
        fs, seconds, segments = 512, 8.0, [(2.6, 8.0)]
        time = np.arange(int(seconds * fs)) / fs
        signal = _eeg(time, rng) + 0.9 * _window(time, segments[0][0], 9.0, ramp=0.3) * \
            _band_noise(time.size, fs, 30, 120, rng)
    elif kind == "power_line":
        # Contamination at the frequency of the power line (60 Hz here)
        fs, seconds, segments = 1024, 1.5, [(0.65, 1.5)]
        time = np.arange(int(seconds * fs)) / fs
        signal = _eeg(time, rng) + 0.9 * _window(time, segments[0][0], 4.0, ramp=0.08) * \
            np.sin(2 * np.pi * 60 * time)
    elif kind == "baseline_variation":
        # A slow shift of the baseline (below 0.4 Hz), from breathing or sweat
        fs, seconds, segments = 128, 30.0, [(8.0, 24.0)]
        time = np.arange(int(seconds * fs)) / fs
        drift = np.sin(2 * np.pi * 0.17 * (time - segments[0][0]))
        signal = 0.6 * _eeg(time, rng) + 4.0 * _window(time, *segments[0], ramp=2.5) * drift
    elif kind == "muscle":
        # Bursts of muscle activity (20-32 Hz and above)
        fs, seconds, segments = 512, 8.0, [(2.9, 4.9), (6.2, 7.0)]
        time = np.arange(int(seconds * fs)) / fs
        envelope = sum(_window(time, start, end, ramp=0.15) for start, end in segments)
        ragged = 0.6 + 0.4 * np.abs(_band_noise(time.size, fs, 0.5, 4, rng))
        signal = _eeg(time, rng) + 1.8 * envelope * ragged * _band_noise(time.size, fs, 20, 90, rng)
    else:
        raise ValueError(kind)
    return time, signal, segments


# The scale bar of each illustration (seconds)
SCALE = {"flatline": 1, "high_frequency_burst": 1, "persistent_noise": 1, "power_line": 0.25,
         "baseline_variation": 5, "muscle": 1}
LABEL = {"flatline": "Flatline", "high_frequency_burst": "High frequency burst", "persistent_noise": "Persistent noise",
         "power_line": "Power line (60 Hz)", "baseline_variation": "Baseline variation", "muscle": "Muscle artifact"}


def draw_artifact(painter, width, height, palette, font, kind, show_name=True):
    """ Draw the illustration of an artifact in a width x height area, in the colors of the theme (palette):
        the EEG in the text color, the artifact in the link color on a light band, the name of the artifact
        above it (unless show_name is False: the page writes it next to the drawing) and a scale bar. """
    time, signal, segments = simulated_artifact(kind)
    painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

    small = QtGui.QFont(font)
    small.setPixelSize(13)
    painter.setFont(small)
    label_height = QtGui.QFontMetrics(small).height()
    left, right = 2.0, width - 2.0
    top = label_height + 6.0 if show_name else 6.0
    bottom = height - label_height - 6.0
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

    # The bands of the artifact first, then the EEG, then the artifact over it
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setBrush(band)
    pieces = []
    for start, end in segments:
        indexes = np.nonzero((time >= start) & (time <= end))[0]
        pieces.append(indexes)
        x0, x1 = x[indexes[0]], x[indexes[-1]]
        painter.drawRoundedRect(QtCore.QRectF(x0 - 4, top - 4, x1 - x0 + 8, bottom - top + 8), 6, 6)
    painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
    painter.setPen(QtGui.QPen(muted, 1.0))
    painter.drawPath(path(np.arange(time.size)))
    painter.setPen(QtGui.QPen(link, 1.2))
    for indexes in pieces:
        painter.drawPath(path(indexes))

    # The name above the first segment (kept inside the area), the scale bar at the bottom left
    if show_name:
        metrics = QtGui.QFontMetrics(small)
        name_width = metrics.horizontalAdvance(LABEL[kind]) + 4
        name_x = min(max(left, x[pieces[0][0]] - 4), right - name_width)
        painter.setPen(QtGui.QPen(link))
        painter.drawText(QtCore.QRectF(name_x, 0, name_width, label_height),
                         QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, LABEL[kind])
    scale = SCALE[kind] * (right - left) / (time[-1] - time[0])
    scale_y = height - label_height / 2 - 1
    painter.setPen(QtGui.QPen(muted, 1.5))
    painter.drawLine(QtCore.QPointF(left, scale_y), QtCore.QPointF(left + scale, scale_y))
    scale_text = f"{SCALE[kind]:g} s"
    painter.drawText(QtCore.QRectF(left + scale + 6, height - label_height - 1, 60, label_height),
                     QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, scale_text)


class ArtifactDrawing(QtCore.QObject):
    """ Paints the illustration of an artifact on its label, at the width of the label, when the label is
        painted: sharp on every screen and in the colors of the theme. The label has no picture. """
    def __init__(self, label, kind, height=LARGE_HEIGHT, show_name=True):
        super().__init__(label)
        self._kind = kind
        self._show_name = show_name
        label.setPixmap(QtGui.QPixmap())
        label.setMinimumHeight(height)
        label.setMaximumHeight(height)
        label.installEventFilter(self)

    def eventFilter(self, label, event):
        if event.type() == QtCore.QEvent.Type.Paint:
            painter = QtGui.QPainter(label)
            draw_artifact(painter, label.width(), label.height(), label.palette(), label.font(), self._kind,
                          self._show_name)
            painter.end()
            return True
        return super().eventFilter(label, event)
