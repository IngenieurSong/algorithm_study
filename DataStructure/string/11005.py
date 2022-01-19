n, b = map(int, input().split())
board = [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
num_list = []

while(n != 0):
    num_list.append(str(board[n % b]))
    n = n // b

for i in range(len(num_list)):
    print(num_list[-1 - i], end = "")
