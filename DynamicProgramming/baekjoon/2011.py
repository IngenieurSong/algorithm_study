board = list(map(int, list(input())))
cache = [0] * (len(board) + 1)
cache[0] = 1
cache[1] = 1

if(board[0] == 0):
    print(0)
else:
    board = [0] + board
    for i in range(2, len(board), 1):
        num1 = board[i]
        num2 = board[i - 1] * 10 + board[i]
        if(num1 > 0):
            cache[i] += cache[i - 1]
        if(num2 >= 10 and num2 <= 26):
            cache[i] += cache[i - 2]

    print(cache[len(board) - 1] % 10000000)
