from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.type = "Square"

    def list_subtypes(self):
        return ["Square"]
