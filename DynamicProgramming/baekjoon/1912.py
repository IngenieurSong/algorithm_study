n = int(input())
board = list(map(int, input().split()))
cache = [0] * n
cache[0] = board[0]

for i in range(1, n, 1):
    cache[i] = max(cache[i - 1] + board[i], board[i])

print(max(cache))
