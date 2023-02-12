def moar(a, b, n):
    return len([_ for _ in a if not _ % n]) > len([_ for _ in b if not _ % n])
