import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start, graph, visited):
    count = 1
    queue = deque([])
    visited[start] = 1
    queue.append(start)

    while(queue):
        node = queue.popleft()

        for i in graph[node]:
            if(not visited[i]):
                visited[i] = 1
                queue.append(i)
                count += 1

    return count

compare = [0] * (n + 1)
for i in range(1, n + 1, 1):
    visited = [0] * (n + 1)
    compare[i] = bfs(i, graph, visited)

for i in range(1, n + 1, 1):
    if(compare[i] == max(compare)):
        print(i, end = " ")
