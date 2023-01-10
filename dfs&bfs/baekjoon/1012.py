from collections import deque

t = int(input())
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if(not visited[nx][ny] and board[nx][ny]):
                visited[nx][ny] = 1
                queue.append((nx, ny))

for _ in range(t):
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    for i in range(n):
        for j in range(m):
            if(not visited[i][j] and board[i][j]):
                bfs(i, j, visited)
                count += 1

    print(count)
