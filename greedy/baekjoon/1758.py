n = int(input())
board = [int(input()) for _ in range(n)]
board.sort(reverse = True)
board = [0] + board
answer = 0

for i in range(1, n + 1, 1):
    if(board[i] - (i - 1) > 0):
        answer += board[i] - (i - 1)

print(answer)
