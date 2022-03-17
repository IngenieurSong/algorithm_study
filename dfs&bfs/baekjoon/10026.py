import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
vector = [(1, 0), (0, -1), (0, 1), (-1, 0)]

def bfs_1(x, y, graph, visited):
    queue = deque([])
    visited[x][y] = 1
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]):
                visited[nx][ny] = 1
                queue.append((nx, ny))

def bfs_2(x, y, graph, visited):
    queue = deque([])
    visited[x][y] = 1
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < n and 0 <= ny < n and not visited[nx][ny]):
                if(graph[x][y] in ['R', 'G'] and graph[nx][ny] in ['R', 'G']):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif(graph[x][y] in ['B'] and graph[nx][ny] in ['B']):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
count1 = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if(visited1[i][j] == 0):
            bfs_1(i, j, graph, visited1)
            count1 += 1

for i in range(n):
    for j in range(n):
        if(visited2[i][j] == 0):
            bfs_2(i, j, graph, visited2)
            count2 += 1

print(count1, count2)
