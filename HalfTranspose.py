a = [list(eval(input()))]
n = len(a[0])
a = a + [list(eval(input())) for _ in range(n - 1)]

for k in range(n):
    print(*(a[k][j] for j in range(k)), *(a[i][k] for i in range(k, -1, -1)), sep=",")
