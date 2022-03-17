n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cache = [[0] * 3 for _ in range(n)]
cache[0][0] = board[0][0]
cache[0][1] = board[0][1]
cache[0][2] = board[0][2]

for i in range(1, n, 1):
    for j in range(3):
        if(j == 0):
            cache[i][j] = min(board[i][j] + cache[i - 1][1], board[i][j] + cache[i - 1][2])
        elif(j == 1):
            cache[i][j] = min(board[i][j] + cache[i - 1][0], board[i][j] + cache[i - 1][2])
        else:
            cache[i][j] = min(board[i][j] + cache[i - 1][0], board[i][j] + cache[i - 1][1])

print(min(cache[n - 1]))
