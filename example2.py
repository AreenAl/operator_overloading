class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __repr__(self):
        return f'Vector({self.x_comp}, {self.y_comp})'

    def __str__(self):
        return f'{self.x_comp}i{self.y_comp:+}j'

vector = Vector(3, 4)

str(vector)
#'3i+4j'

repr(vector)
#'Vector(3, 4)'

b = eval(repr(vector))
type(b), b.x_comp, b.y_comp
#(__main__.Vector, 3, 4)

vector  # Looking at object; __repr__ used
'Vector(3, 4)'