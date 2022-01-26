import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(v, graph, parent):
    for i in graph[v]:
        if(parent[i] == 0):
            parent[i] = v
            dfs(i, graph, parent)

dfs(1, graph, parent)
for i in range(2, n + 1, 1):
    print(parent[i])
