n = int(input())
board = list(map(int, input().split()))
cache = [1] * n

for i in range(1, n, 1):
    for j in range(i):
        if(board[i] > board[j]):
            cache[i] = max(cache[i], cache[j] + 1)

print(max(cache))
