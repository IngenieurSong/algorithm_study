n = int(input())
cache = [-1] * (n + 1)
cache[3] = 1

for i in range(4, n + 1, 1):
    if(i == 5):
        cache[5] = 1
    else:
        if(cache[i - 3] == -1 and cache[i - 5] == -1):
            continue
        compare = [100000, 100000]
        if(cache[i - 3] != -1):
            compare[0] = cache[i - 3] + 1
        if(cache[i - 5] != -1):
            compare[1] = cache[i - 5] + 1

        cache[i] = min(compare)

print(cache[n])
