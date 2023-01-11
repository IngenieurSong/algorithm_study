import heapq
import sys
input = sys.stdin.readline

start, target = map(int, input().split())
distance = [float("inf")] * 100001

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if(now == target):
            break
        if(distance[now] < dist):
            continue

        for i in [(now + 1, 1), (now - 1, 1), (now * 2, 0)]:
            cost = dist + i[1]

            if(i[0] < 0 or i[0] > 100000):
                continue
            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
print(distance[target])
