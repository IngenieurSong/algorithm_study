n = int(input())
time_list = sorted(list(map(int, input().split())))
sum = 0

for i in range(1, n + 1, 1):
    for j in range(0, i, 1):
        sum += time_list[j]

print(sum)
