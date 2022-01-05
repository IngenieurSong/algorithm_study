n = int(input())
cache = [0] * (n + 1)

for i in range(3):
    cache[i] = i
if(n < 3):
    print(cache[n])
else:
    for i in range(3, n + 1, 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    print(cache[n])
