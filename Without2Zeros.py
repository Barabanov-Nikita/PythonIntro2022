def No_2Zero(n, k):
    if n <= 1:
        return (k - 2) * n + 1
    else:
        return (No_2Zero(n - 1, k) + No_2Zero(n - 2, k)) * (k - 1)

