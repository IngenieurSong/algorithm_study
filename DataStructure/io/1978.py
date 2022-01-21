cache = [1] * 1001
cache[0] = 0
cache[1] = 0
prime = []
count = 0

for i in range(2, 1001, 1):
    if(cache[i]):
        prime.append(i)

        for j in range(i * 2, 1001, i):
            cache[j] = 0

n = int(input())
board = list(map(int, input().split()))

for i in board:
    if(i in prime):
        count += 1

print(count)
