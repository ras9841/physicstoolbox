from sympy.physics.units import Dimension

class Tensor:
    def __init__(self, rank):
        self._tRank = rank
        self.units = Dimension("")
    def withUnitsOf(self, unit):
        if type(unit) is Dimension:
            self.units = unit
        else:
            self.units = Dimension(str(unit))
        return self
    def changeUnitsTo(self, unit):
        self.withUnitsOf(unit)

