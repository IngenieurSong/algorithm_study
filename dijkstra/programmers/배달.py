import heapq

inf = int(1e9)

def djikstra(graph, start, n, k):
    result = 0
    queue = []
    distance = [inf] * (n + 1)
    heapq.heappush(queue, (0, start))

    while(queue):
        dist, now = heapq.heappop(queue)

        if(distance[now] < dist):
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if(distance[i[1]] > cost):
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))

    for i in range(2, len(distance), 1):
        if(distance[i] <= k):
            result += 1

    return result + 1

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))

    result = djikstra(graph, 1, N, K)

    return result
