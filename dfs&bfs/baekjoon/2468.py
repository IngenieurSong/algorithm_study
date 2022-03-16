from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
vector = [(1, 0), (0, -1), (0, 1), (-1, 0)]
result = -float("inf")

def bfs(x, y, visited):
    queue = deque([])
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < n and 0 <= ny < n and not visited[nx][ny]):
                visited[nx][ny] = 1
                queue.append((nx, ny))

for i in range(101):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for j in range(n):
        for k in range(n):
            if(graph[j][k] <= i):
                visited[j][k] = 1

    for j in range(n):
        for k in range(n):
            if(visited[j][k] == 0):
                bfs(j, k, visited)
                count += 1

    if(count == 0):
        print(result)
        break

    result = max(result, count)
