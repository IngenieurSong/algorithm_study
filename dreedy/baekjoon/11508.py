n = int(input())
board = [int(input()) for _ in range(n)]
board.sort(reverse = True)

for i in range(2, n, 3):
    board[i] = 0

print(sum(board))
