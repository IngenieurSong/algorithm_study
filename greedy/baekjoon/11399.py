n = int(input())
board = sorted(list(map(int ,input().split())))
result = 0

for i in range(n):
    result += sum(board[0:i + 1])

print(result)
