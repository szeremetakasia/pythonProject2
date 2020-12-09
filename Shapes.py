class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a * self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a


import math


class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        # self._a = a

    def calc_surface(self):
        return math.pi * self._a ** 2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


r = Rectangle(5, 6)
print(r)
# r._a = 600
print(r.calc_surface())
r.swap_sides()
print(r)

c = Circle(7)
print(c)
print(c.calc_surface())


# New Triangle

class Triangle:
    def __init__(self, a=10, b=6, c=4):
        self.set_params(a, b, c)

    def set_params(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perim(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return self.__class__.__name__ + " perimeter of [" + str(self.a) + "] plus [" + str(self.b) + "] plus [" + str(
            self.c) + "] " + str(hex(id(self)))


t = Triangle()
print(t)
print(t.calc_perim())


# Equilateral Triangle inheriting from Triangle(t)

class TriangleEqu(Triangle):
    def calc_perim(self):
        return self.a * 3

    def __repr__(self):
        return self.__class__.__name__ + " of [" + str(self.a) + "] at " + str(hex(id(self)))


t2 = TriangleEqu()
print(t2)
print(t2.calc_perim())


# Square inheriting from Rectangle and using the same calc_surface

class Square(Rectangle):
    def __init__(self, a=4, b=4):
        self.set_params(a, b)

sq = Square()
print(sq)
print(sq.calc_surface())
