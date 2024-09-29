from collections import deque
import sys

input = sys.stdin.readline

def dfs(node, graph, visited):
    visited[node] = 1
    print(node, end = ' ')

    for i in sorted(graph[node]):
        if not visited[i]:
            visited[i] = 1
            dfs(i, graph, visited)

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()
        print(node , end = ' ')

        for i in sorted(graph[node]):
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_bfs = [0] * (n + 1)
visited_dfs = [0] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(v, graph, visited_dfs)
print()
bfs(v, graph, visited_bfs)
