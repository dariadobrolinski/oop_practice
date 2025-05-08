class Rectangle:
    def __init__(self, x=0, y=0, width=1, height=1):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._height + self._width)
    
    def contains(self, a, b):
        half_width = self._width / 2
        half_height = self._height / 2
        return (self._x - half_width <= a <= self._x + half_width and
        self._y - half_height <= b <= self._y + half_height)

    
    def scale(self, factor):
        newWidth = self._width * factor
        newHeight = self._height * factor
        return Rectangle(self._x, self._y, newWidth, newHeight)
    
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y and self._width == other._width and self._height == other._height
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __str__(self):
        return f"({self._x}, {self._y}, {self._width}, {self._height})"

