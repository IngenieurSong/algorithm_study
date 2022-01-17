n = int(input())
board = [0] + list(map(int, input().split()))
cache = [0] * (n + 1)
cache[1] = board[1]

for i in range(2, n + 1, 1):
    for j in range(1, i + 1, 1):
        if(cache[i] < cache[i - j] + board[j]):
            cache[i] = cache[i - j] + board[j]

print(cache[n])
