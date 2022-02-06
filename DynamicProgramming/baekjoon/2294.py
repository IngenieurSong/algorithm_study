n, m = map(int, input().split())
board = [int(input()) for _ in range(n)]
cache = [float("inf")] * (m + 1)
cache[0] = 0

for i in range(1, m + 1, 1):
    for j in board:
        if(i - j >= 0):
            cache[i] = min(cache[i], cache[i - j] + 1)

if(cache[m] == float("inf")):
    print(-1)
else:
    print(cache[m])
