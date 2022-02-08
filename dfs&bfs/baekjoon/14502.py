import sys
import copy
import itertools
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
vector = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def bfs(x, y, graph):
    queue = deque([])
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < n and 0 <= ny < m):
                if(graph[nx][ny] == 0):
                    graph[nx][ny] = 5
                    queue.append((nx, ny))

comb = []

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            comb.append((i, j))

comb = list(itertools.combinations(comb, 3))
max_n = -float("inf")

for k in comb:
    graph_n = copy.deepcopy(graph)
    graph_n[k[0][0]][k[0][1]] = 1
    graph_n[k[1][0]][k[1][1]] = 1
    graph_n[k[2][0]][k[2][1]] = 1
    count = 0

    for i in range(n):
        for j in range(m):
            if(graph_n[i][j] == 2):
                bfs(i, j, graph_n)

    for i in graph_n:
        count += i.count(0)

    max_n = max(max_n, count)

print(max_n)
