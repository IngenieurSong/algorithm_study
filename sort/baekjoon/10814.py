n = int(input())
board = [[i] + list(map(str, input().split())) for i in range(1, n + 1, 1)]

board.sort(key = lambda x : (int(x[1]), x[0]))
for i in board:
    print(i[1], i[2])
