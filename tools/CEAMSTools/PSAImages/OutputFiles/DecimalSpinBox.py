from qtpy.QtWidgets import QDoubleSpinBox


class DecimalSpinBox(QDoubleSpinBox):
    """Accept either decimal separator while displaying values in the Qt locale."""

    def _localized_text(self, text: str) -> str:
        separator = self.locale().decimalPoint()
        return text.translate(str.maketrans({".": separator, ",": separator}))

    def validate(self, text: str, position: int):
        state, _, _ = super().validate(self._localized_text(text), position)
        return state, text, position

    def valueFromText(self, text: str) -> float:
        return super().valueFromText(self._localized_text(text))

    def textFromValue(self, value: float) -> str:
        """ Show only the decimals the value needs, at least two: 0 is 0.00 (as the fields with two decimals)
            and 0.00001 stays 0.00001 (y-min keeps five decimals for a logarithmic Y axis). """
        text = super().textFromValue(value)
        separator = self.locale().decimalPoint()
        if self.decimals() > 2 and separator in text:
            whole, fraction = text.split(separator, 1)
            text = f"{whole}{separator}{fraction.rstrip('0').ljust(2, '0')}"
        return text
