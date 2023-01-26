n, k = map(int, input().split())
board = [int(input()) for _ in range(n)]
cache = [1] + [0] * k

for j in board:
    for i in range(1, k + 1, 1):
        if(i - j < 0):
            continue
        cache[i] += cache[i - j]

print(cache[k])
