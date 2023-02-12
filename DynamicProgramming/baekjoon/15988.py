t = int(input())

cache = [1] * 1000001
cache[2] = 2

for i in range(3, 1000001, 1):
    cache[i] = cache[i - 3] % 1000000009 + cache[i - 2] % 1000000009 + cache[i - 1] % 1000000009

for _ in range(t):
    n = int(input())
    print(cache[n] % 1000000009)
