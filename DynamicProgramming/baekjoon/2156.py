n = int(input())
board = [0] + [int(input()) for _ in range(n)]
cache = [0] * (n + 1)
cache[1] = board[1]

if(n > 1):
    cache[2] = board[1] + board[2]

for i in range(3, n + 1, 1):
    cache[i] = max(cache[i - 1], cache[i - 2] + board[i], cache[i - 3] + board[i - 1] + board[i])

print(max(cache))
