from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def rain(height, visited):
    for i in range(n):
        for j in range(n):
            if(board[i][j] <= height):
                visited[i][j] = 1

def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            if(graph[nx][ny] != 0 and not visited[nx][ny]):
                queue.append((nx, ny))
                visited[nx][ny] = 1

count_list = [1]
count = 1
while count:
    count = 0
    visited = [[0] * n for _ in range(n)]
    rain(len(count_list), visited)

    for i in range(n):
        for j in range(n):
            if(board[i][j] and not visited[i][j]):
                count += 1
                bfs(i, j, board, visited)

    count_list.append(count)

print(max(count_list))
