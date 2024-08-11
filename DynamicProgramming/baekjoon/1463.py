n = int(input())
cache = [int(1e9)] * (n + 1)
cache[n] = 0

for i in range(n, 0, -1):
    if(n % 3 == 0):
        cache[i // 3] = min(cache[i // 3], cache[i] + 1)
    if(n % 2 == 0):
        cache[i // 2] = min(cache[i // 2], cache[i] + 1)
    if(i > 0):
        cache[i - 1] = min(cache[i - 1], cache[i] + 1)

print(cache[1])
