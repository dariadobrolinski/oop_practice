import math

class SineWave:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def coeffs(self):
        return self._a, self._b, self._c
    
    def __getitem__(self, x):
        return self._a * math.sin(self._b * x + self._c)
    
    def amplitude(self):
        return self._a
    
    def period(self):
        return (2 * math.pi) / self._b
    
    def __eq__(self, other):
        return self.amplitude() == other.amplitude() and self.period() == other.period()
    
    def __str__(self):
        return f"f(x) = {self._a}sin({self._b}x + {self._c})"