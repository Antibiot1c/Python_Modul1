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
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        x4, y4 = self.vertices[3]
        
        area = 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - y1*x2 - y2*x3 - y3*x4 - y4*x1)
        return area

    def get_diagonals_lengths(self):
        d1 = math.sqrt((self.vertices[2][0] - self.vertices[0][0]) ** 2 + (self.vertices[2][1] - self.vertices[0][1]) ** 2)
        d2 = math.sqrt((self.vertices[3][0] - self.vertices[1][0]) ** 2 + (self.vertices[3][1] - self.vertices[1][1]) ** 2)
        return [d1, d2]

    def is_convex(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        x4, y4 = self.vertices[3]
        
        AB = (x2 - x1, y2 - y1)
        BC = (x3 - x2, y3 - y2)
        
        CD = (x4 - x3, y4 - y3)
        DA = (x1 - x4, y1 - y4)
        
        cross_product1 = AB[0] * BC[1] - AB[1] * BC[0]
        cross_product2 = BC[0] * CD[1] - BC[1] * CD[0]
        cross_product3 = CD[0] * DA[1] - CD[1] * DA[0]
        cross_product4 = DA[0] * AB[1] - DA[1] * AB[0]
        
        return (cross_product1 > 0 and cross_product2 > 0 and
                cross_product3 > 0 and cross_product4 > 0)

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
        self_sides = self.get_side_segments()

        other_sides = other.get_side_segments()

        for self_side in self_sides:
            for other_side in other_sides:
                if self.do_segments_intersect(self_side, other_side):
                    return True

        return False

    def get_side_segments(self):
        segments = []
        vertices = self.vertices
        for i in range(4):
            segments.append((vertices[i], vertices[(i + 1) % 4]))

        return segments

    def do_segments_intersect(self, segment1, segment2):
        (x1, y1), (x2, y2) = segment1
        (x3, y3), (x4, y4) = segment2

        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            elif val > 0:
                return 1
            else:
                return -1

        o1 = orientation((x1, y1), (x2, y2), (x3, y3))
        o2 = orientation((x1, y1), (x2, y2), (x4, y4))
        o3 = orientation((x3, y3), (x4, y4), (x1, y1))
        o4 = orientation((x3, y3), (x4, y4), (x2, y2))

        if o1 != o2 and o3 != o4:
            return True

        if (o1 == 0 and self.on_segment((x1, y1), (x3, y3), (x2, y2))) or \
           (o2 == 0 and self.on_segment((x1, y1), (x4, y4), (x2, y2))) or \
           (o3 == 0 and self.on_segment((x3, y3), (x1, y1), (x4, y4))) or \
           (o4 == 0 and self.on_segment((x3, y3), (x2, y2), (x4, y4))):
            return True

        return False

    def on_segment(self, p, q, r):
        if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
            return True
        return False
