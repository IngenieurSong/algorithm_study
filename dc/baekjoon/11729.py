import sys
sys.setrecursionlimit(1000000)

n = int(input())
history = []

def hanoi(n, a, b, c):
    if(n == 1):
        history.append((a, c))
        return 0
    else:
        hanoi(n - 1, a, c, b)
        history.append((a, c))
        hanoi(n - 1, b, a, c)

hanoi(n, 1, 2, 3)
print(len(history))
for i in history:
    print(i[0], i[1])
