a, b, c = eval(input())
if a == 0:
    if b:
        print(c / b)
    else:
        print(0 if c else -1)
else:
    d = b**2 - 4*a*c
    if d < 0:
        print(0)
    elif d == 0:
        print(-b / (2 * a))
    else:
        print(*sorted(((- b - d**.5) / (2 * a), (- b + d**.5) / (2 * a))))
