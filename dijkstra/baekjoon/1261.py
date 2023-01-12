import heapq

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
distance = [[float("inf")] * m for _ in range(n)]
vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dijkstra(x, y):
    queue = []
    heapq.heappush(queue, (0, (x, y)))
    distance[x][y] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if(distance[now[0]][now[1]] < dist):
            continue
        for nx, ny in vector:
            nx = now[0] + nx
            ny = now[1] + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            cost = dist + graph[nx][ny]

            if(distance[nx][ny] > cost):
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, (nx, ny)))

dijkstra(0, 0)
print(distance[n - 1][m - 1])
