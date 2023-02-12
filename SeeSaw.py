from itertools import zip_longest, tee


def seesaw(seq):
    even, odd = tee(seq, 2)
    even, odd = filter(lambda x: not x % 2, even), filter(lambda x: x % 2, odd)
    for pair in zip_longest(even, odd, fillvalue=None):
        for elem in pair:
            if elem is not None:
                yield elem
