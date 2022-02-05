n = int(input())
cache = [0] * (n + 1)
cache[1] = 1

for i in range(2, n + 1, 1):
    cache[i] = float("inf")
    j = 1

    while(j ** 2 <= i):
        cache[i] = min(cache[i], cache[i - j ** 2] + 1)
        j += 1

print(cache[n])
