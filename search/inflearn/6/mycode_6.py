import sys

# sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
sum_cross1 = 0
sum_cross2 = 0
sum_max = 0

for i in range(n):
    sum_row = 0
    sum_column = 0
    sum_cross1 += a[i][i]
    sum_cross2 += a[i][-1-i]
    for j in range(n):
        sum_row += a[i][j]
        sum_column += a[j][i]

    sum_max = max(sum_max, sum_row, sum_column)

sum_max = max(sum_max, sum_cross1, sum_cross1)

print(sum_max)
