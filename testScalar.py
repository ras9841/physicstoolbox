import unittest
from scalar import Scalar
from sympy.physics.units import Dimension

class ScalarUnitTest(unittest.TestCase):
    valA = -2
    valB = 3
    def setUp(self):
        self.scalarA = Scalar(self.valA).withUnitsOf("N")
        self.scalarB = Scalar(self.valB).withUnitsOf("m")
        self.scalarC = Scalar(self.valA)
    def tearDown(self):
        del self.scalarA
        del self.scalarB

class ScalarCreation(ScalarUnitTest):
    def test__init__(self):
        s = Scalar()
        self.assertEqual(s, 0)
        self.assertEqual(s.units, Dimension(""))
        self.assertEqual(s._tRank, 0)
        s = Scalar(self.valA)
        self.assertEqual(s, self.valA)
        s = Scalar().withValue(7).withUnitsOf("m")
        self.assertEqual(s.units, self.scalarB.units)
    def test__str__(self):
        self.assertEqual(str(self.scalarA), "-2.0 Dimension(N)")
        self.assertEqual(str(self.scalarB), "3.0 Dimension(m)")
        self.assertEqual(str(self.scalarC), "-2.0 Dimension()")
    def test__eq__(self):
        self.assertEqual(self.scalarA, -2)
        self.assertEqual(self.scalarA, -2.0)
        self.assertFalse(self.scalarA == 2001)
        self.assertFalse(self.scalarA == self.scalarB)
        self.assertFalse(self.scalarA == self.scalarC)

if __name__ == '__main__':
    unittest.main()
        
