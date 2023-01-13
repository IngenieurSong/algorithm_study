n = int(input())
board = [int(input()) for _ in range(n)]
board.sort()
weight = 0

for i in range(n):
    weight = max(weight, board[i] * (n - i))

print(weight)
