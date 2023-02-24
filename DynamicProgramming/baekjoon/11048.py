n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vector = [(1, 0), (0, 1), (1, 1)]
cache = [[-float("inf")] * m for _ in range(n)]
cache[0][0] = board[0][0]

for i in range(n):
    for j in range(m):
        for nx, ny in vector:
            nx = i + nx
            ny = j + ny

            if(0 > nx or n <= nx or 0 > ny or m <= ny):
                continue
            cache[nx][ny] = max(cache[nx][ny], cache[i][j] + board[nx][ny])

print(cache[n - 1][m - 1])
