from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, graph):
    queue = deque([])
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < n and 0 <= ny < m):
                if(graph[nx][ny] == 1):
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

bfs(0, 0, graph)
print(graph[n - 1][m - 1])
