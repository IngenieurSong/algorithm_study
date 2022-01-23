from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(graph, m, n, queue_b):
    queue_a = deque([])

    while(queue_b):
        x, y = queue_b.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0):
                graph[nx][ny] = 1
                queue_a.append((nx, ny))

    return queue_a

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
queue_b = deque([])
count = -1

for i in range(m):
    for j in range(n):
        if (graph[i][j] == 1):
            queue_b.append((i, j))

while(True):
    if(not queue_b):
        for i in graph:
            if(i.count(0)):
                count = -1
                break

        print(count)
        break

    count += 1
    queue_b = bfs(graph, m, n, queue_b)
