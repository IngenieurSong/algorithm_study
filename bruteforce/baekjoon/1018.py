n, m = map(int, input().split())
board = []
count = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        index_1 = 0
        index_2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        index_1 += 1
                    if board[k][l] != 'B':
                        index_2 += 1
                else:
                    if board[k][l] != 'B':
                        index_1 += 1
                    if board[k][l] != 'W':
                        index_2 += 1
        count.append(min(index_1, index_2))

print(min(count))
