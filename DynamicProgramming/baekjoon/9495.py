t = int(input())
for _ in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    cache = [[0] * n for _ in range(2)]
    cache[0][0] = board[0][0]
    cache[1][0] = board[1][0]

    for i in range(1, n, 1):
        cache[0][i] = max(cache[0][i - 1], cache[1][i - 1] + board[0][i])
        cache[1][i] = max(cache[1][i - 1], cache[0][i - 1] + board[1][i])

    print(max(max(cache[0]), max(cache[1])))
