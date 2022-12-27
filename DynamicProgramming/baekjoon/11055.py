n = int(input())
board = [0] + list(map(int, input().split()))
cache = [0] * (n + 1)
cache[1] = board[1]

for i in range(2, n + 1, 1):
    for j in range(1, i, 1):
        if(board[i] > board[j]):
            cache[i] = max(cache[i], cache[j] + board[i])
        else:
            cache[i] = max(cache[i], board[i])

print(max(cache))
