import decimal
from math import factorial

decimal.getcontext().prec = 10000


def PiGen():
    s, k, elem, x = 13591409, 1, 1, 13591409
    while True:
        elem = decimal.Decimal(elem * 8 * (6*k + 1) * (6*k + 3) * (6*k + 5)) / ((k + 1) * (k + 1) * (k + 1) * (-262537412640768000))
        x += 545140134
        s += elem * x
        pi = s / (decimal.Decimal(426880) * decimal.Decimal(10005).sqrt())
        k += 1
        yield decimal.Decimal(1) / pi


print(262537412640768000/8)
# for i, p in enumerate(PiGen()):
#     if i>120:
#         break
# print(str(p)[1400:1470])