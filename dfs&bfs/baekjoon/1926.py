from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vector = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def bfs(graph, x, y):
    area = 1
    queue = deque([(x, y)])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(0 > nx or n <= nx or 0 > ny or m <= ny):
                continue
            if(graph[nx][ny] == 1):
                area += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return area

areas = []
for i in range(n):
    for j in range(m):
        if(board[i][j] == 1):
            areas.append(bfs(board, i, j))

print(len(areas))
print(max(areas) if len(areas) != 0 else 0)
