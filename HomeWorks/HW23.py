# Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
# вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.
import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def dist_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x1, y1)

    def __str__(self):
        return f'(radius={self.radius}, ' + super().__str__()[1:]

    def __sub__(self, other):
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        if self.radius == other.radius:
            return Point(x, y)
        else:
            radius_new = abs(self.radius - other.radius)
            return radius_new, x, y


a = Circle(5, 2, 3)
b = Circle(5, 5, 7)
c = a - b
print(a)
print(b)
print(c)

