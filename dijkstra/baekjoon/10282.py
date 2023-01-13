import heapq

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [float("inf")] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)
    safe = distance.count(float("inf"))
    distance = sorted(distance, reverse = True)
    print(len(distance) - safe, distance[safe])
