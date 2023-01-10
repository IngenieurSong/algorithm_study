from collections import deque

def bfs(start, graph, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = 1

    while queue:
        node = queue.popleft()
        print(node, end = ' ')

        for i in sorted(graph[node]):
            if(not visited_bfs[i]):
                visited_bfs[i] = 1
                queue.append(i)

def dfs(node, graph, visited_dfs):
    visited_dfs[node] = 1
    print(node, end = ' ')

    for i in sorted(graph[node]):
        if(not visited_dfs[i]):
            visited_dfs[i] = 1
            dfs(i, graph, visited_dfs)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_bfs = [0] * (n + 1)
visited_dfs = [0] * (n + 1)

dfs(v, graph, visited_dfs)
print()
bfs(v, graph, visited_bfs)
