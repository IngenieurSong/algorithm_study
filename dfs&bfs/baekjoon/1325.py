import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 1
    count = 0

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if(not visited[i]):
                count += 1
                visited[i] = 1
                queue.append(i)

    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[end].append(start)

result_list = [0]

for i in range(1, n + 1, 1):
    visited = [0] * (n + 1)
    result_list.append(bfs(i, graph, visited))

comp_num = max(result_list)
for i in range(1, n + 1, 1):
    if(comp_num == result_list[i]):
        print(i, end = ' ')
