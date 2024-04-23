import math

class Quadrilateral:
    def __init__(self, vertices):
        self.vertices = vertices
        self.type = "Quadrilateral"

    def get_vertex_coordinates(self):
        return self.vertices

    def get_side_lengths(self):
        sides = []
        for i in range(4):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % 4]
            length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            sides.append(length)
        return sides

    def perimeter(self):
        lengths = self.get_side_lengths()
        return sum(lengths)

    def area(self):
        pass

    def get_diagonals_lengths(self):
        pass

    def is_convex(self):
        pass

    def list_subtypes(self):
        return ["Quadrilateral"]

    def list_supertypes(self):
        return ["Quadrilateral"]

    def check_type_membership(self, type_to_check):
        return isinstance(self, type_to_check)

    def compare_area(self, other):
        if isinstance(other, Quadrilateral):
            return self.area() == other.area()
        return False

    def compare_perimeter(self, other):
        if isinstance(other, Quadrilateral):
            return self.perimeter() == other.perimeter()
        return False

    def compare_area_and_perimeter(self, other):
        if isinstance(other, Quadrilateral):
            return self.area() == other.area() and self.perimeter() == other.perimeter()
        return False

    def intersects(self, other):
        pass
