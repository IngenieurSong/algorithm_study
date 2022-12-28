from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
stride = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, graph):
    queue = deque([(x, y)])
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in stride:
            nx = x + nx
            ny = y + ny

            if(nx <= -1 or nx >= n or ny <= -1 or ny >= n):
                continue
            if(graph[nx][ny] == 0):
                continue
            graph[nx][ny] = 0
            count += 1
            queue.append((nx, ny))

    return count

result = []
for i in range(n):
    for j in range(n):
        if(graph[i][j]):
            result.append(bfs(i, j, graph))

print(len(result))
for i in sorted(result):
    print(i)
