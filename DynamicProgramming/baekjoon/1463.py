n = int(input())
cache = [float("inf")] * (n + 1)
cache[1] = 0

for i in range(2, n + 1, 1):
    if(i % 3 == 0):
        cache[i] = min(cache[i], cache[i // 3] + 1)
    if(i % 2 == 0):
        cache[i] = min(cache[i], cache[i // 2] + 1)
    cache[i] = min(cache[i], cache[i - 1] + 1)

print(cache[n])
