t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    cache = [[0] * n for _ in range(2)]
    cache[0][0] = sticker[0][0]
    cache[1][0] = sticker[1][0]

    for i in range(1, n, 1):
        for j in range(2):
            if(j == 0):
                cache[j][i] = max(cache[j][i - 1], cache[j + 1][i - 1] + sticker[j][i])
            else:
                cache[j][i] = max(cache[j][i - 1], cache[j - 1][i - 1] + sticker[j][i])

    print(max(cache[0][n - 1], cache[1][n - 1]))
