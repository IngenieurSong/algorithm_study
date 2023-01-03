t = int(input())

def resident_count():
    k = int(input())
    n = int(input())
    cache = [[1] * n for _ in range(k + 1)]
    for i in range(1, n + 1, 1):
        cache[0][i - 1] = i

    for i in range(1, k + 1, 1):
        for j in range(n):
            cache[i][j] = sum(cache[i - 1][0 : j + 1])

    print(cache[k][n - 1])

for _ in range(t):
    resident_count()
