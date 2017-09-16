import unittest
from scalar import Scalar
from sympy.physics.units import Dimension

class ScalarUnitTest(unittest.TestCase):
    valA = -2
    valB = 3
    def setUp(self):
        self.scalarA = Scalar(self.valA).withUnitsOf("N")
        self.scalarB = Scalar(self.valB).withUnitsOf("m")
    def tearDown(self):
        del self.scalarA
        del self.scalarB

class ScalarCreation(ScalarUnitTest):
    def testMakeScalar(self):
        s = Scalar()
        self.assertEqual(s, 0)
        self.assertEqual(s.units, Dimension(""))
        s = Scalar(self.valA)
        self.assertEqual(s, self.valA)

if __name__ == '__main__':
    unittest.main()
        
