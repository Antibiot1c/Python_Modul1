from quadrilateral import Quadrilateral
import math

class Rhombus(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.type = "Rhombus"

    def area(self):
        side = self.get_side_lengths()[0]
        diagonal1, diagonal2 = self.get_diagonals_lengths()
        area = (diagonal1 * diagonal2) / 2
        return area

    def is_convex(self):
        return True

    def get_diagonals_lengths(self):
        d1 = math.sqrt((self.vertices[2][0] - self.vertices[0][0]) ** 2 + (self.vertices[2][1] - self.vertices[0][1]) ** 2)
        d2 = math.sqrt((self.vertices[3][0] - self.vertices[1][0]) ** 2 + (self.vertices[3][1] - self.vertices[1][1]) ** 2)
        return [d1, d2]

    def list_subtypes(self):
        return ["Rhombus"]

    def intersects(self, other):
        pass
