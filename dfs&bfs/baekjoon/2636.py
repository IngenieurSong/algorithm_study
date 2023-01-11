import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
count = 0
vector = [(1, 0), (0, -1), (0, 1), (-1, 0)]

def bfs(x, y, graph):
    visited = [[0] * m for _ in range(n)]
    queue = deque([])
    graph[x][y] = 5
    queue.append((x, y))
    chcnt = 0

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                if(graph[nx][ny] == 1):
                    graph[nx][ny] = 5
                    chcnt += 1
                else:
                    graph[nx][ny] = 5
                    queue.append((nx, ny))

    return chcnt

while(exit):
    ch_count = bfs(0, 0, graph)
    count += 1

    for i in graph:
        if(1 in i):
            exit = 1
            break
    else:
        exit = 0

print(count)
print(ch_count)
  
# 풀이 2
from collections import deque

vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    count_cheese = 0

    while queue:
        x, y = queue.popleft()

        for nx, ny in vector:
            nx = x + nx
            ny = y + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if(not visited[nx][ny]):
                if(graph[nx][ny] == 0):
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif(graph[nx][ny]):
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    count_cheese += 1

    return count_cheese

count_cheese = []

def main(n, m, board):
    count = 0
    for i in range(n):
        for j in range(m):
            visited = [[0] * m for _ in range(n)]
            if(not visited[i][j] and board[i][j] == 0):
                count_cheese.append(bfs(i, j, board, visited))

                if(count_cheese[-1] == 0):
                    print(count)
                    print(count_cheese[-2])
                    return 0
                count += 1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

main(n, m, board)
