mport sys

# sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

for i in range(0, n, 1):
    for j in range(0, n - i, 1):
        sum = 0
        for k in range(j, j + i + 1, 1):
            sum += num_list[k]
        if(sum == m):
            count += 1

print(count)
