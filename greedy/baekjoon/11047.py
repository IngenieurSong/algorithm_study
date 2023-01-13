n, k = map(int, input().split())
board = sorted([int(input()) for _ in range(n)], reverse = True)
coin = 0

for i in board:
    if(k // i == 0):
        continue
    coin += k // i
    k = k % i

print(coin)
