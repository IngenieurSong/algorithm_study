n, k = map(int, input().split())
board = [[0, 0]]
cache = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n + 1, 1):
    for j in range(1, k + 1, 1):
        w = board[i][0]
        v = board[i][1]

        if(j < w):
            cache[i][j] = cache[i - 1][j]
        else:
            cache[i][j] = max(cache[i - 1][j], cache[i - 1][j - w] + v)

print(cache[n][k])
