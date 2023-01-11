from collections import deque

t = int(input())
vector = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, -1), (-2, 1), (-1, -2), (-1, 2)]

def bfs(x_s, y_s, x_e, y_e, graph, visited):
    queue = deque([(x_s, y_s)])
    visited[x_s][y_s] = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx == x_e and ny == y_e):
                graph[nx][ny] = graph[x][y] + 1
                return

            if(nx < 0 or nx >= l or ny < 0 or ny >= l):
                continue
            if(graph[nx][ny] == 0 and not visited[nx][ny]):
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for _ in range(t):
    l = int(input())
    x_s, y_s = map(int, input().split())
    x_e, y_e = map(int, input().split())

    if(x_s == x_e and y_s == y_e):
        print(0)
        continue

    visited = [[0] * l for _ in range(l)]
    board = [[0] * l for _ in range(l)]
    board[x_s][y_s] = 1

    bfs(x_s, y_s, x_e, y_e, board, visited)
    print(board[x_e][y_e] - 1)
