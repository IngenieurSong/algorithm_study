n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = []
max_sum = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1, 1):
        for k in range(j + 1, n, 1):
            sum_list.append(num_list[i] + num_list[j] + num_list[k])

for i in sum_list:
    if(i <= m and i > max_sum):
        max_sum = i

print(max_sum)
