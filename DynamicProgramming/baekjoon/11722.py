n = int(input())
board = [-float("inf")] + list(map(int, input().split()))
cache = [1] * (n + 1)

for i in range(2, n + 1, 1):
    for j in range(i):
        if(board[i] < board[j]):
            cache[i] = max(cache[i], cache[j] + 1)

print(max(cache))
