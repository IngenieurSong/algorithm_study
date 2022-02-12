board = list(map(str, input()))
i = 0

while(board.count("X") != 0):
    if(board[i] == "."):
        i += 1
        continue
    if(len(board) - i >= 4 and board[i:i + 4].count("X") == 4):
        for j in range(i, i + 4, 1):
            board[j] = "A"
        i += 4
    elif(len(board) - i >= 2 and board[i:i + 2].count("X") == 2):
        for j in range(i, i + 2, 1):
            board[j] = "B"
        i += 2
    else:
        print(-1)
        break
else:
    print(''.join(board))
