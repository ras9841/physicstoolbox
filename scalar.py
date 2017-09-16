from tensor import Tensor

class Scalar(float, Tensor):
    def __init__(self, val=0):
        self._value = float.__new__(float, val)
        Tensor.__init__(self, rank=0)
    ### MAGIC METHODS ###
    def __str__(self):
        return str(self._value)+" "+str(self.units)
    def __eq__(self, s):
        return self._value == s
    ### MAGIC MATH METHODS ###
    def __add__(self, s):
        if self.units is not s.units:
            raise TypeError("Cannot add scalars of different types!")
        return Scalar(self._value+s._value).withUnitsOf(self.units)
    def __sub__(self, s):
        if self.units is not s.units:
            raise TypeError("Cannot subtract scalars of different types!")
        return Scalar(self._value-s._value).withUnitsOf(self.units)
    def __mul__(self, s):
        units = self.units*s.units
        return Scalar(self._value*s._value).withUnitsOf(units)
    def __div__(self, s):
        if s._value == 0.0:
            raise ZeroDivisionError("Cannot divide by zero!")
        units = self.units/s.units
        return Scalar(self._value/s._value).withUnitsOf(units)
    ### OTHER METHODS ###
    def withValue(self, val):
        self._value = float.__new__(float, val)
        return self
