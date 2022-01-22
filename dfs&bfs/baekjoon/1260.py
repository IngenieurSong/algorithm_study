import sys
from collections import deque

input = sys.stdin.readline

def dfs(v, graph, visited):
    visited[v] = 1
    graph[v].sort()
    print(v, end = " ")

    for i in graph[v]:
        if(not visited[i]):
            dfs(i, graph, visited_d)

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = 1

    while(queue):
        v = queue.popleft()
        print(v, end = " ")
        graph[v].sort()

        for i in graph[v]:
            if(not visited[i]):
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = list([] for _ in range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited_d = [0] * (n + 1)
visited_b = [0] * (n + 1)

dfs(v, graph, visited_d)
print()
bfs(v, graph, visited_b)
