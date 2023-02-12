k = int(input())
n = 1
while (k * 10**n - k**2) % (10 * k - 1):
    n += 1

print(1 if k == 1 else (k * 10**n - k**2) // (10 * k - 1) * 10 + k)
