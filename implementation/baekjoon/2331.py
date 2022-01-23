import sys
imput = sys.stdin.readline

a, p = map(int, input().split())
board = [str(a)]
idx = 0

while(True):
    element = 0

    for i in board[idx]:
        element += int(i) ** p

    if(str(element) not in board):
        board.append(str(element))
        idx += 1

    else:
        board = board[:board.index(str(element))]
        print(len(board))
        break
