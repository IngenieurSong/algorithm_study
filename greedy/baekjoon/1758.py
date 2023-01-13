n = int(input())
board = [int(input()) for _ in range(n)]
board = sorted(board, reverse = True)
result = 0

for i in range(n):
    result += max(board[i] - i, 0)

print(result)
