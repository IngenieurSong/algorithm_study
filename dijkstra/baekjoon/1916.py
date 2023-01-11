import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [float("inf")] * (n + 1)

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

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

            if(cost < distance[i[0]]):
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
