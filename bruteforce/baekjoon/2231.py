n = int(input())
num_list = []

for i in range(1, n + 1, 1):
    sum = i
    for j in str(i):
        sum += int(j)

    if(sum == n):
        num_list.append(i)

min_sum = 2147483647
for i in num_list:
    if(min_sum > i):
        min_sum = i

print(min_sum)
