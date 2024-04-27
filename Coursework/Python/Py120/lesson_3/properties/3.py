class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        raise AttributeError('Unable to modify width')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        raise AttributeError('Unable to modify width')

r = Rectangle(3,5)
print(r.width)
print(r.height)
r.width = 6
print(r.width)
