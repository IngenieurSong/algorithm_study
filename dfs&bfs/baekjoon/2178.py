from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y, graph):
    queue = deque([(x, y)])
    stride = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for nx, ny in stride:
            nx = x + nx
            ny = y + ny

            if(nx <= -1 or nx >= n or ny <= -1 or ny >= m):
                continue
            if(graph[nx][ny] == 0):
                continue
            if(graph[nx][ny] == 1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0, graph))
