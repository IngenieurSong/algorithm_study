n = int(input())
cache = [0] * (n + 1)

for i in range(1, n + 1, 1):
    if(i == 1 or i == 2):
        cache[i] = i
        continue

    cache[i] = min(cache[i - 1] + 1, cache[i - 3] + 1)

if(cache[n] % 2 != 0):
    print("SK")
else:
    print("CY")
