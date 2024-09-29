from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start, graph):
    queue = deque([start])
    parent = [i for i in range(n + 1)]
    parent[start] = start

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if parent[i] == i:
                parent[i] = node
                queue.append(i)

    return parent

parent = bfs(1, graph)

for i in range(2, n + 1, 1):
    print(parent[i])
