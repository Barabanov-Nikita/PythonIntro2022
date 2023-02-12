import decimal


func, prec = input(), int(input())
decimal.setcontext(decimal.Context(prec=prec + 2, rounding=decimal.ROUND_CEILING))
e = decimal.Decimal("0." + "0" * prec + "1")
l = decimal.Decimal("-1.5")
r = decimal.Decimal("1.5")

while r - l > e:
    x = (l + r) / 2
    if (y := eval(func)) > 0:
        r = x
    else:
        l = x

print(f"{l:.{prec}f}")
