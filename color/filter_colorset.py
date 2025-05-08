import stdio
import sys
from color import Color
from colorset import ColorSet

def main():
    colorSet = ColorSet()

    while not stdio.isEmpty():
        r = stdio.readInt()
        g = stdio.readInt()
        b = stdio.readInt()

        color = Color(r, g, b)
        colorSet.add(color)

    stdio.writeln("Colors: " + str(colorSet))
    stdio.writeln("Average: " + str(colorSet.average()))
    stdio.writeln("Brightest: " + str(colorSet.brightest()))

if __name__ == '__main__':
    main()