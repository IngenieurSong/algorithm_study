import heapq

n = int(input())
schedules = sorted([list(map(int, input().split())) for _ in range(n)])
heap = []

for s, e in schedules:
    if(heap and heap[0] <= s):
        heapq.heappop(heap)
    heapq.heappush(heap, e)

print(len(heap))
