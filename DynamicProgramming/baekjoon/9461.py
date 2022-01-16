t = int(input())
for _ in range(t):
    n = int(input())
    cache = [0, 1, 1]
    
    for i in range(3, n + 1, 1):
        cache.append(cache[i - 3] + cache[i - 2])

    print(cache[n])
