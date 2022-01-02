n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0

for i in range(len(coins)):
    if(k // coins[-1 - i] != 0):
        count += k // coins[-1 - i]
        k = k % coins[-1 - i]

print(count)
