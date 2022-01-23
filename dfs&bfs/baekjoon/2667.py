import sys
from collections import deque

def bfs(x, y, graph):
    queue = deque([])
    queue.append((x, y))
    count = 0

    while(queue):
        x, y = queue.popleft()

        if(graph[x][y] == 1):
            if(x - 1 > -1):
                queue.append((x - 1, y))
            if(x + 1 < n):
                queue.append((x + 1, y))
            if(y - 1 > -1):
                queue.append((x, y - 1))
            if(y + 1 < n):
                queue.append((x, y + 1))

            graph[x][y] = 0
            count += 1

    return count

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
count = []

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            count.append(bfs(i, j, graph))

print(len(count))
count.sort()
for i in count:
    print(i)
