n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

zero = 0
minus = 0
plus = 0

def check(x, y, n):
    global zero, minus, plus

    num_check = board[x][y]

    for i in range(x, x + n, 1):
        for j in range(y, y + n, 1):
            if(board[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        check(x + k * (n // 3), y + l * (n // 3), n // 3)
                return 0

    if(num_check == 0):
        zero += 1
    elif(num_check == -1):
        minus += 1
    else:
        plus += 1

check(0, 0, n)
print(minus)
print(zero)
print(plus)
