n = int(input())
board = list(map(str, input()))

count = [1, 0]
comp = board[0]
flag = 0

for i in board:
    if(i != comp):
        flag = not flag
        comp = i
        count[flag] += 1

print(1 + min(count))
