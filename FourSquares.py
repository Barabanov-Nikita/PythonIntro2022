n = int(input())

for x in range(int(n**0.5/4), int(n**0.5) + 1):
    for y in range(int((n - x**2)**0.5/3), min(x, int((n - x**2)**0.5)) + 1):
        for z in range(int((n - x**2 - y**2)**0.5/2), min(y, int((n - x**2 - y**2)**0.5)) + 1):
            t = int((n - x**2 - y**2 - z**2)**0.5)
            if n == x**2 + y**2 + z**2 + t**2 and t <= z:
                print(x, y, z, t)