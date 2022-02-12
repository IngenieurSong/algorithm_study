n = int(input())
board = [int(input()) for _ in range(n)]
board.sort()
max_sum = 0

for i in range(n):
    if(max_sum < board[i] * (n - i)):
        max_sum = board[i] * (n - i)

print(max_sum)
