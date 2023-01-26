n, k = map(int, input().split())
board = [int(input()) for _ in range(n)]
cache = [0] + [float("inf")] * k

for i in range(1, k + 1, 1):
    for j in board:
        if(i - j >= 0):
            cache[i] = min(cache[i], cache[i - j] + 1)

print(cache[k] if cache[k] != float("inf") else -1)
