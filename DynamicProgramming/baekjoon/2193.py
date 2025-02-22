n = int(input())
cache = [[0] * 2 for _ in range(n + 1)]
cache[1][1] = 1

for i in range(2, n + 1, 1):
    cache[i][0] = cache[i - 1][0] + cache[i - 1][1]
    cache[i][1] = cache[i - 1][0]

print(sum(cache[n]))
