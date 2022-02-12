n = int(input())
cache = [0, float("inf"), 1, float("inf"), 2]

for i in range(5, n + 1, 1):
    cache.append(min(cache[i - 2] + 1, cache[i - 5] + 1))

print(-1 if cache[n] == float("inf") else cache[n])
