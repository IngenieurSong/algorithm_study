from collections import deque

t = int(input())

def bfs(start, graph, visited):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if(i == start):
                return 1
            queue.append(i)
            visited[i] = 1

    return 0

for _ in range(t):
    n = int(input())
    board = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(len(board))]
    visited = [0] * len(board)
    count = 0

    for i in range(1, len(board), 1):
        graph[i].append(board[i])

    for i in range(1, len(board), 1):
        if(not visited[i]):
            count += bfs(i, graph, visited)

    print(count)
