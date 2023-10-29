from collections import deque

vector = [(1, 0), (0, -1), (0, 1), (-1, 0)]

def bfs(board, visit, x, y):
    queue = deque([(x, y)])
    visit[x][y] = 1
    count = 1

    while(queue):
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue

            if(board[nx][ny] == 0 and not visit[nx][ny]):
                visit[nx][ny] = 1
                queue.append((nx, ny))
                count += 1

    return count

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
visit = [[0] * m for _ in range(n)]
result = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(n - y2, n - y1, 1):
        for j in range(x1, x2, 1):
            board[i][j] = 1

for i in range(n):
    for j in range(m):
        if(board[i][j] == 0 and not visit[i][j]):
            result.append(bfs(board, visit, i, j))

print(len(result))
for i in sorted(result):
    print(i, end = ' ')
