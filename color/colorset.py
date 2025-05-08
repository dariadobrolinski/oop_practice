from color import Color

class ColorSet:
    def __init__(self):
        self._colors = []

    def add(self, color):
        self._colors.append(color)

    def average(self):
        totalR = sum(color.getRed() for color in self._colors)
        totalG = sum(color.getGreen() for color in self._colors)
        totalB = sum(color.getBlue() for color in self._colors)

        avgR = int(totalR / len(self._colors))
        avgG = int(totalG / len(self._colors))
        avgB = int(totalB / len(self._colors))

        return Color(avgR, avgG, avgB)
    
    def brightest(self):
        return max(self._colors, key=lambda c: c.luminosity())

    def contains(self, color):
        return color in self._colors
    
    def __str__(self):
        return str([str(color) for color in self._colors])
    
def _main():
    c1 = Color(255, 0, 0)
    c2 = Color(0, 255, 0)
    c3 = Color(0, 0, 255)

    cs = ColorSet()
    cs.add(c1)
    cs.add(c2)
    cs.add(c3)

    print("All colors:", cs)
    print("Average:", cs.average())
    print("Brightest:", cs.brightest())
    print("Contains red?", cs.contains(Color(255, 0, 0)))
    print("Contains white?", cs.contains(Color(255, 255, 255)))

if __name__ == '__main__':
    _main()
