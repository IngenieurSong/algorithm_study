t = int(input())
n_list = []
for _ in range(t):
    n_list.append(int(input()))

for i in n_list:
    cache = [0, 1, 2, 4] * 5
    if(i < 3):
        print(cache[i])
    else:
        for j in range(4, i + 1, 1):
            cache[j] = cache[j - 3] + cache[j - 2] + cache[j - 1]
        print(cache[i])
