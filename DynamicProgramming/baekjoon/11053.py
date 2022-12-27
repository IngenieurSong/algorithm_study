n = int(input())
board = [0] + list(map(int, input().split()))
cache = [1] * (n + 1)

for i in range(1, n + 1, 1):
    for j in range(1, i, 1):
        if(board[i] > board[j]):
            cache[i] = max(cache[i], cache[j] + 1)

print(max(cache))
