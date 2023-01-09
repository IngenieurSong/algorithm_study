n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cache = [[0] * n for _ in range(n)]
cache[0][0] = 1

for i in range(n):
    for j in range(n):
        if(cache[i][j] == 0 or (i == n - 1 and j == n - 1)):
            continue
        vector = [(0, board[i][j]), (board[i][j], 0)]

        for nx, ny in vector:
            nx = i + nx
            ny = j + ny

            if(nx < n and ny < n):
                cache[nx][ny] += cache[i][j]

print(cache[n - 1][n - 1])
