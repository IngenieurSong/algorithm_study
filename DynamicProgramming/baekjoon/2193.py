n = int(input())
cache = [0] * (n + 1)

cache[1] = 1
for i in range(2, n + 1, 1):
    cache[i] = cache[i - 2] + cache[i - 1]

print(cache[n])

# 2차원 dp 풀이
n = int(input())
cache = [[0] * (n + 1) for _ in range(2)]
cache[1][1] = 1

for column in range(2, n + 1, 1):
    for row in range(2):
        if(row == 0):
            cache[row][column] = cache[row][column - 1] + cache[row + 1][column - 1]
        else:
            cache[row][column] = cache[row - 1][column - 1]
print(cache[0][n] + cache[1][n])
