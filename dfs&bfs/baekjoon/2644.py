from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
board = [[] for _ in range(n + 1)]

def bfs(graph, visited, node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if(not visited[i]):
                visited[i] = visited[node] + 1
                queue.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0] * (n + 1)
count = bfs(board, visited, p1)
print(visited[p2] if visited[p2] else -1)
