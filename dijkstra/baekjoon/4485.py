import heapq

def dijkstra(x, y, vector):
    queue = []
    heapq.heappush(queue, (graph[x][y], (x, y)))
    distance[x][y] = graph[x][y]

    while queue:
        dist, now = heapq.heappop(queue)

        if(distance[now[0]][now[1]] < dist):
            continue

        for nx, ny in vector:
            nx = now[0] + nx
            ny = now[1] + ny

            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue

            cost = dist + graph[nx][ny]

            if(distance[nx][ny] > cost):
                distance[nx][ny] = cost
                heapq.heappush(queue, (cost, (nx, ny)))

count = 0
while(True):
    count += 1
    n = int(input())
    if(n == 0):
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[float("inf")] * n for _ in range(n)]
    vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dijkstra(0, 0, vector)
    print(f"Problem {count}:", distance[n - 1][n - 1])
