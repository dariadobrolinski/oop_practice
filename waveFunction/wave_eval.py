import sys
import stdio
from sinewave import SineWave

def main():
    x = float(sys.argv[1])

    waves = []

    while not stdio.isEmpty():
        a = stdio.readFloat()
        b = stdio.readFloat()
        c = stdio.readFloat()

        wave = SineWave(a, b, c)
        waves.append(wave)

        print(f"{str(wave)}; f({x}) = {round(wave[x], 2)}; amplitude = {wave.amplitude()}; period = {round(wave.period(), 2)}")

if __name__ == '__main__':
    main()