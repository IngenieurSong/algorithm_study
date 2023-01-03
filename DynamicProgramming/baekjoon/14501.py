k = int(input())
board = [list(map(int, input().split())) for _ in range(k)]
cache = [0] * (k + 1)

for i in range(k - 1, -1 ,-1):
    if(i + board[i][0] > k):
        cache[i] = cache[i + 1]
    else:
        cache[i] = max(cache[i + 1], cache[i + board[i][0]] + board[i][1])

print(cache[0])
