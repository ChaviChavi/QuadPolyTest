from math import pi


class QuadraticPolynomial:
    def __init__(self, a, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if (self.b) ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if (self.b) ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, args):
        a, b, c = args
        self.a, self.b, self.c = a, b, c



