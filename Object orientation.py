class Rectangle:

    def set_params(self, a, b):
        self.a = a
        self.b = b

    def calc_surface(self):
        return self.a * self.b


r = Rectangle()
r.set_params(6, 6)
print(r.calc_surface())
