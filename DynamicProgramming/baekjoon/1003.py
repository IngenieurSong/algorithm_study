t = int(input())
cache = [(1, 0)] * 41
cache[1] = (0, 1)

for _ in range(t):
    n = int(input())

    for i in range(2, n + 1, 1):
        cache[i] = (cache[i - 2][0] + cache[i - 1][0], cache[i - 2][1] + cache[i - 1][1])

    print(cache[n][0], cache[n][1])
