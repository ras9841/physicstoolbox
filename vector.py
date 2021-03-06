import numpy as np
from tensor import Tensor
from scalar import Scalar
from sympy.physics.units import Dimension

class Vector(Tensor):
    componentMap = dict({
        ("x", 0), ("y", 1), ("z", 2),
        ("i", 0), ("j", 1), ("k", 2),
        ("rho", 0), ("theta", 1), ("phi", 2)
    })
    def __init__(self, dim=3):
        super().__init__(1)
        self._values = np.zeros(dim)
        self.dimension = dim
    def __str__(self):
        return "["+", ".join(map(str,self._values))+"] "+str(self.units)
    def __add__(self, vec):
        if self.units != vec.units:
            raise TypeError("Cannot add vectors of different units!")
        elif self.dimension != vec.dimension:
            raise AttributeError("Cannot add vectors of different dimension!")
        result = Vector(self.dimension)
        result.units = self.units
        result._values = self._values + vec._values
        return result
    def __sub__(self, vec):
        if self.units != vec.units:
            raise TypeError("Cannot add vectors of different units!")
        elif self.dimension != vec.dimension:
            raise AttributeError("Cannot add vectors of different dimension!")
        result = Vector(self.dimension)
        result.units = self.units
        result._values = self._values - vec._values
        return result
    def __len__(self):
        return self.dimension
    def withComponent(self, component, val):
        if type(component) is str:
            component = self.componentMap[component]
        
        if component < self.dimension:
            self._values[component] = val
        else:
            raise IndexError("Cannot insert value at component %s!"%component)
        return self
    def changeComponent(self, component, val):
        self.withComponent(component, val)
    def dottedWith(self, vec):
        if type(vec) is not Vector:
            raise TypeError("The dot product requires two vectors!")
        elif vec.dimension is not self.dimension:
            raise TypeError("Vectors must be the same dimension!")
        units = self.units*vec.units
        return Scalar(np.vdot(self._values,vec._values)).withUnitsOf(units)
    def crossedWith(self, vec):
        if type(vec) is not Vector:
            raise TypeError("The cross product requires two vectors!")
        elif self.dimension is not 3 and vec.dimension is not 3:
            raise AttributeError("The cross product is only defined in three dimensions!")
        result = Vector().withUnitsOf(self.units*vec.units)
        result._values = np.cross(self._values, vec._values)
        return result

