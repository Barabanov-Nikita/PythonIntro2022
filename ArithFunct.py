def ADD(f, g):
    return lambda x: (f(x) if callable(f) else f) + (g(x) if callable(g) else g)


def SUB(f, g):
    return lambda x: (f(x) if callable(f) else f) - (g(x) if callable(g) else g)


def MUL(f, g):
    return lambda x: (f(x) if callable(f) else f) * (g(x) if callable(g) else g)


def DIV(f, g):
    return lambda x: (f(x) if callable(f) else f) / (g(x) if callable(g) else g)

