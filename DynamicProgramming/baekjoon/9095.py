t = int(input())

for _ in range(t):
    n = int(input())
    cache = [i for i in range(n + 1)]
    cache[0] = 1

    for i in range(3, n + 1, 1):
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]

    print(cache[n])
