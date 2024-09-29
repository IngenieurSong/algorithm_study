from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1
    count = 0

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                count += 1

    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)

count_list = [0] * (n + 1)

for i in range(1, n + 1, 1):
    count_list[i] = bfs(i, graph)

max_count = max(count_list)

for i in range(1, n + 1, 1):
    if(count_list[i] == max_count):
        print(i, end = ' ')
