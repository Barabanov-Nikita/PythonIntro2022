from random import uniform
from math import atan2, sin, cos


def randsquare(a, b):
    diag = (b[0] - a[0], b[1] - a[1])
    l = (diag[0] * diag[0] + diag[1] * diag[1])**.5 / (2**.5)
    x, y = uniform(0, l), uniform(0, l)
    angle = atan2(*diag) - atan2(l, l)
    x, y = x * cos(angle) + y * sin(angle), - x * sin(angle) + y * cos(angle)
    x, y = x + a[0], y + a[1]
    return x, y

for i in range(100000):
    x, y = randsquare((0,-10.01), (0,10.01))
    if x**2+y**2 > 100:
        print(f"Error: {x}:{y}")