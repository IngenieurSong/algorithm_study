n = int(input())
board = list(map(int, input().split()))
cache = [i for i in board]

for i in range(1, n, 1):
    for j in range(i):
        if (board[i] > board[j]):
            cache[i] = max(cache[i], cache[j] + board[i])

print(max(cache))
