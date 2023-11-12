
class FreeVibrationResult:

    def __init__(self, natural_frequencies: list, mode_shapes: list) -> None:
        """Results from the free vibration analysis.

        :param natural_frequencies: List of natural frequencies in Hz.
        :param mode_shapes: List of mode shapes.
        """
        self._natural_frequencies = natural_frequencies
        self._mode_shapes = mode_shapes

    def natural_frequencies(self) -> list:
        return self._natural_frequencies

    def mode_shapes(self) -> list:
        return self._mode_shapes
