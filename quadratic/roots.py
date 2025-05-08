import sys
import stdio
from quadratic import Quadratic 

def main():
    x = float(sys.argv[1])

    while not stdio.isEmpty():
        a = stdio.readFloat()
        b = stdio.readFloat()
        c = stdio.readFloat()

        quadratic = Quadratic(a, b, c)

        print(str(quadratic))
        print(f"f({x}) = {quadratic[x]}")
        print(f"Roots: {quadratic.roots()}")
        print(f"Sum: {quadratic.sum_of_roots()}")
        print(f"Product: {quadratic.prod()}")

if __name__ == '__main__':
    main()

