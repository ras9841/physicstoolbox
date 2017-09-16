from vector import Vector
from scalar import Scalar

def calculateWork():
    force = Vector().withComponent("x",1).withComponent("z",3).withUnitsOf("N")
    dist = Vector().withComponent("x",5).withComponent("y",3).withUnitsOf("m")
    work = force.dottedWith(dist)
    print("Force =", force) 
    print("Dist  =", dist) 
    print("Work  =", work)

def calculateTorque():
    radius = Vector().withComponent("i",1).withUnitsOf("m")
    force = Vector().withComponent("k",1).withUnitsOf("N")
    torque = radius.crossedWith(force)
    print("Radius =", radius) 
    print("Force  =", force) 
    print("Torque =", torque)

def examples():
    calculateWork()
    calculateTorque()

if __name__ == "__main__":
    examples()
