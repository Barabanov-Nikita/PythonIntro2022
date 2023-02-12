from collections import Counter
from math import sqrt


class Spiral:
    def __init__(self, string, counter=None):
        self.string = string
        self.spiral = counter if counter else Counter(string)
        self.n = int((-1 + sqrt(1 + 8 * self.spiral.total())) / 2) + 2
        self.start = self.n // 2

    def __str__(self):
        matrix = [[" "] * self.n for _ in range(self.n)]
        x, y, i, m = self.start, self.start, 0, 1
        v = 0, 1
        for elem in self.spiral.elements():
            matrix[x][y] = elem
            x, y, i = x + v[0], y + v[1], i + 1
            if i >= m:
                v = -v[1], v[0]
                i, m = 0, m + 1

        matrix = ["".join(_) for _ in matrix]
        r = len(matrix[0])
        m = min(r - len(_.lstrip()) for _ in matrix)
        matrix = [_[m:].rstrip() for _ in matrix]
        matrix = [_ for _ in matrix if _]
        return "\n".join(matrix)

    def __add__(self, other):
        return Spiral("", self.spiral + other.spiral)

    def __sub__(self, other):
        return Spiral("", self.spiral - other.spiral)

    def __mul__(self, other):
        return Spiral(self.string * other)

    def __iter__(self):
        return iter(self.spiral.elements())

