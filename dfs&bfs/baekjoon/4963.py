from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(x, y, graph, h, w):
    queue = deque([])
    queue.append((x, y))
    graph[x][y] = 0

    while(queue):
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1):
                graph[nx][ny] = 0
                queue.append((nx, ny))

while(True):
    w, h = map(int, input().split())
    count = 0

    if(w == 0 or h == 0):
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if(graph[i][j] == 1):
                bfs(i, j, graph, h, w)
                count += 1

    print(count)
