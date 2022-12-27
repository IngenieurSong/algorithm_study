# 풀이 1
n = int(input())
cache = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    cache[1][i] = 1

for i in range(2, n + 1, 1):
    for j in range(0, 10, 1):
        for k in range(0, j + 1, 1):
            cache[i][j] += cache[i - 1][k]

print(sum(cache[n]) % 10007)

# 풀이 2
n = int(input())
cache = [[1] * 10 for _ in range(n + 1)]

for i in range(2, n + 1, 1):
    for j in range(1, 10, 1):
        cache[i][j] = cache[i][j - 1] + cache[i - 1][j]

print(sum(cache[n]) % 10007)
