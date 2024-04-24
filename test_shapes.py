import unittest
from quadrilateral import Quadrilateral
from parallelogram import Parallelogram
from rhombus import Rhombus
from rectangle import Rectangle
from square import Square

class TestQuadrilaterals(unittest.TestCase):
    def setUp(self):
        self.parallelogram = Parallelogram([(0, 0), (3, 1), (5, 4), (2, 3)])
        self.rhombus = Rhombus([(0, 0), (2, 3), (4, 0), (2, -3)])
        self.rectangle = Rectangle([(0, 0), (4, 0), (4, 3), (0, 3)])
        self.square = Square([(0, 0), (2, 0), (2, 2), (0, 2)])

    def test_perimeter(self):
        self.assertAlmostEqual(self.parallelogram.perimeter(), 12.60555127546399, places=10)
        self.assertAlmostEqual(self.rhombus.perimeter(), 14.856406460551018, places=10)
        self.assertAlmostEqual(self.rectangle.perimeter(), 14.0, places=10)
        self.assertAlmostEqual(self.square.perimeter(), 8.0, places=10)

    def test_area(self):
        self.assertAlmostEqual(self.parallelogram.area(), 10.0, places=10)
        self.assertAlmostEqual(self.rhombus.area(), 12.0, places=10)
        self.assertAlmostEqual(self.rectangle.area(), 12.0, places=10)
        self.assertAlmostEqual(self.square.area(), 4.0, places=10)

    def test_convexity(self):
        self.assertTrue(self.parallelogram.is_convex())
        self.assertTrue(self.rhombus.is_convex())
        self.assertTrue(self.rectangle.is_convex())
        self.assertTrue(self.square.is_convex())

    def test_compare_perimeter(self):
        self.assertTrue(self.parallelogram.compare_perimeter(self.rectangle))
        self.assertFalse(self.rhombus.compare_perimeter(self.square))

    def test_intersects(self):
        self.assertTrue(self.parallelogram.intersects(self.rhombus))
        self.assertFalse(self.rectangle.intersects(self.square))

if __name__ == '__main__':
    unittest.main()
