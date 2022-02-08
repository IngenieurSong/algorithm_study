from collections import deque

w, h = map(int, input().split())
graph = [[0] * (w + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(h)] + [[0] * (w + 2)]
vector_o = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, 1)]
vector_e = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1)]

def bfs(x, y, graph):
    queue = deque([])
    count = 0
    queue.append((x, y))
    graph[x][y] = 2

    while(queue):
        x, y = queue.popleft()
        if(x % 2 == 0):
            vector = vector_e
        else:
            vector = vector_o

        for i in vector:
            nx = x + i[0]
            ny = y + i[1]

            if(0 <= nx <= h + 1 and 0 <= ny <= w + 1):
                if(graph[nx][ny] == 0):
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
                elif(graph[nx][ny] == 1):
                    count += 1

    return count

count = bfs(0, 0, graph)
print(count)
