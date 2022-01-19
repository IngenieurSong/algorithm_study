n, b = map(str, input().split())
board = [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
sum = 0

for i in range(len(n)):
    sum += board.index(n[-1 - i]) * (int(b) ** i)

print(sum)
