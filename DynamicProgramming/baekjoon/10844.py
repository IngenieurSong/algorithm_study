n = int(input())
cache = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10, 1):
    cache[1][i] = 1

for i in range(2, n + 1, 1):
    for j in range(10):
        if(j == 0):
            cache[i][j] = cache[i - 1][j + 1]
        elif(j == 9):
            cache[i][j] = cache[i - 1][j - 1]
        else:
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j + 1]

print(sum(cache[n]) % 1000000000)
