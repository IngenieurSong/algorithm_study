from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
count = []
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * n for _ in range(n)]

def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    house = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if(graph[nx][ny] == 1 and not visited[nx][ny]):
                house += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return house

for i in range(n):
    for j in range(n):
        if(board[i][j] == 1 and not visited[i][j]):
            count.append(bfs(i, j, board, visited))

print(len(count))
for i in sorted(count):
    print(i)
