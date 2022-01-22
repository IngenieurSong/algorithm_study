import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = 1

   
    while(queue):
        v = queue.popleft()

        for i in graph[v]:
            if(not visited[i]):
                queue.append(i)
                visited[i] = 1

for i in range(1, n + 1, 1):
    if(not visited[i]):
        bfs(i, graph, visited)
        count += 1

print(str(count))
