from sympy.physics.units import Dimension

class Tensor:
    def __init__(self, rank):
        self._tRank = rank
        self.units = Dimension("")
    def withUnitsOf(self, unit):
        self.units = Dimension(unit)
        return self
    def changeUnitsTo(self, unit):
        self.withUnitsOf(unit)

