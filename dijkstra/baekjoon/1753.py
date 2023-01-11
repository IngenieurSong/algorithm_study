import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [float("inf")] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, v + 1, 1):
    print("INF" if distance[i] == float("inf") else distance[i])
