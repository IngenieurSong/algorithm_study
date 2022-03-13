import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float("inf")] * (n + 1)
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while(queue):
        dist, now = heapq.heappop(queue)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

origin_path = dijkstra(1)
v1_path = dijkstra(v1)
v2_path = dijkstra(v2)

result = min(origin_path[v1] + v1_path[v2] + v2_path[n], origin_path[v2] + v2_path[v1] + v1_path[n])

if(result == float("inf")):
    print(-1)
else:
    print(result)
