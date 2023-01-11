from collections import deque

vector = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]

def bfs(x, y, graph, visited, n, m):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if(graph[nx][ny] == 1 and not visited[nx][ny]):
                visited[nx][ny] = 1
                queue.append((nx, ny))

while(True):
    m, n = map(int, input().split())

    if(n == 0):
        break

    board = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if(board[i][j] == 1 and not visited[i][j]):
                bfs(i, j, board, visited, n, m)
                count += 1

    print(count)
