from collections import deque

n = int(input())
board = [list(map(str, input())) for _ in range(n)]
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if(board[x][y] == board[nx][ny] and not visited[nx][ny]):
                visited[nx][ny] = 1
                queue.append((nx, ny))

def bfs_RGB(x, y, visited_RGB):
    queue = deque([(x, y)])
    visited_RGB[x][y] = 1

    if(board[x][y] in ['R', 'G']):
        target_color = ['R', 'G']
    else:
        target_color = ['B']

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if(not visited_RGB[nx][ny] and board[nx][ny] in target_color):
                visited_RGB[nx][ny] = 1
                queue.append((nx, ny))

count = 0
count_RGB = 0

visited = [[0] * n for _ in range(n)]
visited_RGB = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            bfs(i, j, visited)
            count += 1

for i in range(n):
    for j in range(n):
        if(not visited_RGB[i][j]):
            bfs_RGB(i, j, visited_RGB)
            count_RGB += 1

print(count, count_RGB)
