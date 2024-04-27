class Point:
    def __init__(self, x, y):
        self.coordinates = {'x': x, 'y': y}
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.coordinates['x'] = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.coordinates['y'] = y

    def __eq__(self, other):
        return self.coordinates == other.coordinates

point1 = Point(5, 10)
point2 = Point(5, 10)
point3 = point1
point1.x = 4

print(point1 == point2)
print(point2 == point3)
print(point1 == point3)
print(point1 is point3)
