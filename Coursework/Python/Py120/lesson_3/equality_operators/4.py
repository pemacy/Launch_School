class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector) and not isinstance(other, int):
            return NotImplemented
        if isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        return Vector(self.x + other.y, self.y + other.y)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.y, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.y, self.y - other.y)

    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.y, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Vector) and not isinstance(other, int):
            return NotImplemented
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return Vector(self.x * other.y, self.y * other.y)

    def __imul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x * other.y, self.y * other.y)

    def __rmul__(self, other):
        return self.__mul__(other)

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)             # Vector(8, 16)
print(my_vector)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 8)

print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'
