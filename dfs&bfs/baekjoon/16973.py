from collections import deque
import sys
input = sys.stdin.readline

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h, w, s1, s2, f1, f2 = map(int, input().split())
visited = [[0] * m for _ in range(n)]
s1, s2, f1, f2 = s1 - 1, s2 - 1, f1 - 1, f2 - 1
walls =[]

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            walls.append((row,col,))

def isSatisfied(nrow, ncol):
    if(nrow + h -1 >= n or ncol + w -1 >= m):
        return False

    for w_row, w_col in walls:
        if(nrow <= w_row < nrow + h and ncol <= w_col < ncol + w):
            return False
    return True

def bfs():
    queue =[]
    queue.append((0, s1, s2))
    
    while(queue):
        path, row, col = queue.pop(0)

        if row == f1 and col == f2:
            return path
      
        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow = row + drow
            ncol = col + dcol

            if(nrow < 0 or nrow >= n or ncol < 0 or ncol >= m):
                continue

            if(not isSatisfied(nrow, ncol)):
                continue

            if(not visited[nrow][ncol]):
                visited[nrow][ncol] = 1
                queue.append((path + 1, nrow, ncol))

    return -1

print(bfs())
