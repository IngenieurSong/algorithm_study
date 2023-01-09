c, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cache = [0] + [float("inf")] * c

for i in range(1, c + 1, 1):
    for price, customer in board:
        if(i - customer < 0):
            cache[i] = min(cache[i], price)
            continue
        cache[i] = min(cache[i], cache[i - customer] + price)

print(cache[c])
