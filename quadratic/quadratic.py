import math

class Quadratic:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def coeffs(self):
        return self._a, self._b, self._c
    
    def __getitem__(self, x):
        return self._a * (x ** 2) + self._b * x + self._c
    
    def roots(self):
        r1 = ((-self._b + math.sqrt(self._b ** 2 - (4 * self._a * self._c))) / (2 * self._a))
        r2 = ((-self._b - math.sqrt(self._b ** 2 - (4 * self._a * self._c))) / (2 * self._a))
        return r1, r2
    
    def sum_of_roots(self):
        r1, r2 = self.roots()
        return r1 + r2
    
    def prod(self):
        r1, r2 = self.roots()
        return r1 * r2
    
    def __eq__(self, other):
        return self.sum_of_roots() == other.sum_of_roots() and self.prod() == other.prod()
    
    def __str__(self):
        s = f"{self._a}x^2"
        if self._b < 0:
            s += f" - {-self._b}x"
        elif self._b > 0:
            s += f" + {self._b}x"
        if self._c < 0:
            s += f" - {-self._c}"
        elif self._c > 0:
            s += f" + {self._c}"
        return s