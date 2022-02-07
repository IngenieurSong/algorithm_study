from collections import deque

n = int(input())
m = int(input())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

def bfs(start, graph, visited):
    queue = deque([])
    count = 0
    queue.append(start)
    visited[start] = 1

    while(queue):
        node = queue.popleft()

        for i in graph[node]:
            if(not visited[i]):
                visited[i] = 1
                count += 1
                queue.append(i)
    return count

print(bfs(1, graph, visited))
