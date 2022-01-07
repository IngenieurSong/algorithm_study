t = int(input())
for _ in range(t):
    n = int(input())
    cache = [[0] + list(map(int, input().split())) for _ in range(2)]

    for i in range(2, n + 1, 1):
        cache[0][i] += max(cache[1][i - 2], cache[1][i - 1])
        cache[1][i] += max(cache[0][i - 2], cache[0][i - 1])

    print(max(cache[0][n], cache[1][n]))
