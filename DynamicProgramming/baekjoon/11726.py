n = int(input())
cache = [1] * (n + 1)

for i in range(2, n + 1, 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[n] % 10007)
