from collections import deque

vector = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def bfs(graph, visited, x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    count = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if(not visited[nx][ny] and graph[nx][ny] == 1):
                visited[nx][ny] = 1
                queue.append((nx, ny))
                count += 1

    return count

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
trash = []

for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1 and not visited[i][j]):
            trash.append(bfs(graph, visited, i, j))

print(max(trash))
