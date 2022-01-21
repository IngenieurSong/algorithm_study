n, m = map(int, input().split())
cache = [1] * 1000001
cache[0] = 0
cache[1] = 0
prime = []

for i in range(2, 1000001, 1):
    if(cache[i]):
        for j in range(2 * i, 1000001, i):
            cache[j] = 0

for i in range(n, m + 1, 1):
    if(cache[i] == 1):
        print(i, end = " ")
