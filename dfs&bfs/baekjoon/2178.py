from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, graph):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(0 > nx or nx >= n or 0 > ny or ny >= m):
                continue
            if(graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs(0, 0, board)
print(board[n - 1][m - 1])
