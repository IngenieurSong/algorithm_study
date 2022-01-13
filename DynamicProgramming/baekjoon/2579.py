n = int(input())
board = [0] * 302
cache = [0] * 302

for i in range(1, n + 1, 1):
        board[i] = int(input())

cache[1] = board[1]
cache[2] = board[1] + board[2]
cache[3] = max(board[1] + board[2], board[1] + board[3])

for i in range(4, n + 1, 1):
        cache[i] = max(board[i] + board[i - 1] + cache[i - 3], board[i] + cache[i - 2])

print(cache[n])
