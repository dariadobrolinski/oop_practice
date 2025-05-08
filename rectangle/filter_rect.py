import sys
import stdio
from rectangle import Rectangle

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    w = float(sys.argv[3])
    h = float(sys.argv[4])
    
    rect = Rectangle(x, y, w, h)

    total = 0
    outside = 0

    while not stdio.isEmpty():
        a = stdio.readFloat()
        b = stdio.readFloat()
        total += 1
        if not rect.contains(a, b):
            outside += 1

    stdio.writeln(outside / total)

if __name__ == '__main__':
    main()
