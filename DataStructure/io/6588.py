import sys
input = sys.stdin.readline
print = sys.stdout.write

cache = [1] * 1000001
cache[0] = 0
cache[1] = 0

for i in range(2, 1000001, 1):
    if(cache[i]):
        for j in range(2 * i, 1000001, i):
            cache[j] = 0

cache[2] = 0

while(True):
    n = int(input())

    if(n == 0):
        break
    for i in range(3, n + 1, 1):
        if(cache[i] and cache[n - i]):
            print("{0} = {1} + {2}\n".format(n, i, n - i))
            break
