dots = []
while s := input().split():
    c = [int(i) for i in s[:-1]] + s[-1:]
    if c[2] and c[3]:
        dots.append(c)

x_min, y_min = min(dots, key=lambda x: x[0] + x[2]), min(dots, key=lambda x: x[1] + x[3])
x_alt_min, y_alt_min = min(dots, key=lambda x: x[0])[0], min(dots, key=lambda x: x[1])[1]
x_min, y_min = min(x_min[0] + x_min[2], x_alt_min), min(y_min[1] + y_min[3], y_alt_min)

x_max, y_max = max(dots, key=lambda x: x[0] + x[2]), max(dots, key=lambda x: x[1] + x[3])
x_max, y_max = x_max[0] + x_max[2], y_max[1] + y_max[3]
x_alt_max, y_alt_max = max(dots, key=lambda x: x[2])[2], max(dots, key=lambda x: x[3])[3]
x,  y = max(x_max - x_min, x_alt_max), max(y_max - y_min, y_alt_max)
if not x:
    x = max(dots, key=lambda x: x[2])[2]
if not y:
    y = max(dots, key=lambda x: x[3])[3]

a = [["."] * x for _ in range(y)]
for dot in dots:
    for i in range(dot[0] - x_min - (1 if dot[2] < 0 else 0), dot[0] + dot[2] - x_min - (1 if dot[2] < 0 else 0), 1 if dot[2] > 0 else -1):
        for j in range(dot[1] - y_min - (1 if dot[3] < 0 else 0), dot[1] + dot[3] - y_min - (1 if dot[3] < 0 else 0), 1 if dot[3] > 0 else -1):
            a[j][i] = dot[4]

a = "\n".join(["".join(_) for _ in a])
print(a)
