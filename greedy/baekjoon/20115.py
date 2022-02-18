n = int(input())
board = list(map(int, input().split()))
board.sort(reverse = True)
sum = board[0]

for i in range(1, n, 1):
    sum += board[i] / 2

print("%g"%sum)
