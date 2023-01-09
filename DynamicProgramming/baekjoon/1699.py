n = int(input())
cache = [i for i in range(n + 1)]

for i in range(1, n + 1, 1):
    for j in range(1, i, 1):
        if(j * j > i):
            break
        if(cache[i] > cache[i - j * j] + 1):
            cache[i] = cache[i - j * j] + 1
        # 밑의 코드는 시간 초과
        # cache[i] = min(cache[i], cache[i - j * j] + 1)

print(cache[n])
