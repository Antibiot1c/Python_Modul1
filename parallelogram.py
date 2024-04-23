from quadrilateral import Quadrilateral

class Parallelogram(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.type = "Parallelogram"

    def area(self):
        v1 = (self.vertices[1][0] - self.vertices[0][0], self.vertices[1][1] - self.vertices[0][1])
        v2 = (self.vertices[2][0] - self.vertices[3][0], self.vertices[2][1] - self.vertices[3][1])
        area = abs(v1[0] * v2[1] - v1[1] * v2[0])
        return area

    def get_diagonals_lengths(self):
        d1 = math.sqrt((self.vertices[2][0] - self.vertices[0][0]) ** 2 + (self.vertices[2][1] - self.vertices[0][1]) ** 2)
        d2 = math.sqrt((self.vertices[3][0] - self.vertices[1][0]) ** 2 + (self.vertices[3][1] - self.vertices[1][1]) ** 2)
        return [d1, d2]

    def is_convex(self):
        return True

    def list_subtypes(self):
        return ["Parallelogram"]

    def intersects(self, other):
        pass
