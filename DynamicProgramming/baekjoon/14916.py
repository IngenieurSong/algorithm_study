# 풀이 1
n = int(input())
cache = [0, float("inf"), 1, float("inf"), 2]

for i in range(5, n + 1, 1):
    cache.append(min(cache[i - 2] + 1, cache[i - 5] + 1))

print(-1 if cache[n] == float("inf") else cache[n])

# 풀이 2
n = int(input())
cache = [float("inf")] * (n + 1)
cache[0] = 0
if(n > 1):
    cache[2] = 1

for i in range(3, n + 1, 1):
    if(i - 2 >= 0):
        cache[i] = min(cache[i], cache[i - 2] + 1)
    if(i - 5 >= 0):
        cache[i] = min(cache[i], cache[i - 5] + 1)

if(cache[n] == float("inf")):
    print(-1)
else:
    print(cache[n])
