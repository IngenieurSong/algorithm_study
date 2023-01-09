n = int(input())
board = [0] + [int(input()) for _ in range(n)]
cache = [0] * (n + 1)
cache[1] = board[1]

if(n <= 2):
    print(sum(board))
else:
    for i in range(2, n + 1, 1):
        cache[i] = max(cache[i - 1], cache[i - 2] + board[i], board[i] + board[i - 1] + cache[i - 3])

    print(max(cache))
