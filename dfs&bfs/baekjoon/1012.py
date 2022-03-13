import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
vector = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y, graph):
    queue = deque([])
    graph[x][y] = 2
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1):
                graph[nx][ny] = 2
                queue.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if(graph[i][j] == 1):
                bfs(i, j, graph)
                count += 1

    print(count)
