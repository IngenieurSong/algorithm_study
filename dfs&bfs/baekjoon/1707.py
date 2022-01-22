t = int(input())

def bfs(v, graph, visited):
    visited[v] = 1
    queue = deque([v])
    queue.append(v)

    while(queue):
        a = queue.popleft()

        for i in graph[a]:
            if(visited[i] == 0):
                visited[i] = -visited[a]
                queue.append(i)
            else:
                if(visited[i] == visited[a]):
                    return False
    return True

for i in range(t):
    n, m = map(int, input().split())
    isTrue = True
    graph = [[] for i in range(n + 1)]
    visited = [0 for i in range(n + 1)]

    for j in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for k in range(1, n + 1):
        if(visited[k] == 0):
            if(not bfs(k)):
                isTrue = False
                break

    print("YES"if isTrue else "NO")
