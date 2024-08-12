n = int(input())
cache = [1] * (n + 1)

for i in range(2, n + 1, 1):
    cache[i] = cache[i - 1] + cache[i - 2] # 가로 타일 두개를 쌓거나 세로 타일을 하나 쌓기

print(cache[n] % 10007)
