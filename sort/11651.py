n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

board.sort(key = lambda x : (x[1], x[0]))
for i in board:
    print(i[0], i[1])
