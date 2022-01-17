n, k = map(int, input().split())

board = list(map(int, input().split()))
board = sorted(board)

print(board[k - 1])
