class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def getRed(self):
        return self.r
    
    def getGreen(self):
        return self.g
    
    def getBlue(self):
        return self.b
    
    def luminosity(self):
        return ((0.299 * self.r) + (0.587 * self.g) + (0.114 * self.b))
    
    def __add__(self, other):
        avgR = (self.r + other.r) // 2
        avgG = (self.g + other.g) // 2
        avgB = (self.b + other.b) // 2
        return Color(avgR, avgG, avgB)
    
    def __eq__(self, other):
        return (self.r == other.r and self.g == other.g and self.b == other.b)
    
    def cmp(self, other):
        if self.luminosity() < other.luminosity():
            return -1
        elif self.luminosity() > other.luminosity():
            return 1
        else:
            return 0

    def __str__(self):
        return f"({self.r}, {self.g}, {self.b})"