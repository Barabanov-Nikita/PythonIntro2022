def nomore(seq):
    for elem in seq:
        yield from (_ for _ in seq if _ <= elem)
