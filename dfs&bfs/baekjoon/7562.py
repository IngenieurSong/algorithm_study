from collections import deque

t = int(input())
vector = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def bfs(x, y, graph, l):
    queue = deque([])
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    s1, s2 = map(int, input().split())
    t1, t2 = map(int, input().split())

    if(s1 == t1 and s2 == t2):
        print(0)
        continue

    bfs(s1, s2, graph, l)
    print(graph[t1][t2])
