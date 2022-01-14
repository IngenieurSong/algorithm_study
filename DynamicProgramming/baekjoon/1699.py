n = int(input())
cache = [0] * (n + 1)
index = 0

for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        if(j * j > i):
            index = (j - 1) ** 2
            break

    cache[i] = cache[i - index] + 1

print(cache[n])
