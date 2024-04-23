from quadrilateral import Quadrilateral
from parallelogram import Parallelogram
from rhombus import Rhombus
from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    # Creating instances of different types of quadrilaterals
    parallelogram = Parallelogram([(0, 0), (3, 1), (5, 4), (2, 3)])
    rhombus = Rhombus([(0, 0), (2, 3), (4, 0), (2, -3)])
    rectangle = Rectangle([(0, 0), (4, 0), (4, 3), (0, 3)])
    square = Square([(0, 0), (2, 0), (2, 2), (0, 2)])

    # Printing results
    print("Parallelogram Perimeter:", parallelogram.perimeter())
    print("Parallelogram Area:", parallelogram.area())
    print("Is Parallelogram Convex?", parallelogram.is_convex())
    print("-----------------------------")

    print("Rhombus Perimeter:", rhombus.perimeter())
    print("Rhombus Area:", rhombus.area())
    print("Is Rhombus Convex?", rhombus.is_convex())
    print("-----------------------------")

    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())
    print("Is Rectangle Convex?", rectangle.is_convex())
    print("-----------------------------")

    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Is Square Convex?", square.is_convex())
    print("-----------------------------")
