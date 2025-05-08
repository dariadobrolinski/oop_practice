import random
from color import Color

class RandomColors():
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.n:
            self.count += 1
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            return Color(r, g, b)
        else:
            raise StopIteration