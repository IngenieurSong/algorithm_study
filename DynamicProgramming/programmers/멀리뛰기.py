cache = [1] * (n + 1)

for i in range(2, n + 1, 1):
    cache[i] = cache[i - 2] + cache[i - 1]

return cache[n] % 1234567
