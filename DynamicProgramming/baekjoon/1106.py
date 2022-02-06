import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
cache = [float("inf")] * (n + 1)
cache[0] = 0

for i in range(1, n + 1, 1):
    for j in board:
        if(i - j[1] < 0):
            cache[i] = min(cache[i], j[0])
        else:
            cache[i] = min(cache[i], cache[i - j[1]] + j[0])

print(str(cache[n]))
