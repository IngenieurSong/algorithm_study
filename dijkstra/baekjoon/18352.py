import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
distance = [float("inf")] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append((e, 1))

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

dijkstra(x)
if(distance.count(k) == 0):
    print(-1)
else:
    for i in range(1, n + 1, 1):
        if(distance[i] == k):
            print(i)
