from quadrilateral import Quadrilateral
import math

class Rectangle(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.type = "Rectangle"

    def area(self):
        lengths = self.get_side_lengths()
        return lengths[0] * lengths[1]

    def get_diagonals_lengths(self):
        diagonal1 = math.sqrt((self.vertices[2][0] - self.vertices[0][0]) ** 2 + (self.vertices[2][1] - self.vertices[0][1]) ** 2)
        diagonal2 = math.sqrt((self.vertices[3][0] - self.vertices[1][0]) ** 2 + (self.vertices[3][1] - self.vertices[1][1]) ** 2)
        return [diagonal1, diagonal2]

    def is_convex(self):
        return True

    def list_subtypes(self):
        return ["Rectangle"]

    def intersects(self, other):
        pass
