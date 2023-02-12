n = int(input())
cache = [0] * (n + 1)

if(n > 1):
  cache[2] = 3

for i in range(3, n + 1, 1):
  if(not i % 2):
    cache[i] = cache[i - 2] * 3 + sum(cache[: i - 2] * 2) + 2

print(cache[n])
