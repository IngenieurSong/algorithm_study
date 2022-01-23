import sys
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [0 for i in range(n + 1)]
    count = 0

    board = [0] + list(map(int, input().split()))
    for i in range(1, n + 1, 1):
        graph[i].append(board[i])

    for i in range(1, n + 1, 1):
        if(not visited[i]):
            need_visited = deque([])
            need_visited.append(i)

            while(need_visited):
                node = need_visited.pop()

                if(not visited[node]):
                    visited[node] = 1
                    need_visited.extend(graph[node])

                else:
                    count += 1
                    break
    print(count)
