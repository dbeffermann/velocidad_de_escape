import numpy as np
import sys

g = float(sys.argv[1])

r = float(sys.argv[2])

r = r*1000

ve = np.sqrt(2*g*r)

print(f"La velocidad de escape es: {round(ve,3)} m/s")