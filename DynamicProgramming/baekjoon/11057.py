n = int(input())
cache = [[1] * 10 for _ in range(n + 1)]

for i in range(2, n + 1, 1):
    for j in range(1, 10, 1):
        cache[i][j] = cache[i][j - 1] + cache[i - 1][j]

print(sum(cache[n]) % 10007)
