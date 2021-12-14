import sys

# sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))

c = []

while(len(a) != 0 and len(b) != 0):
    if(a[0] > b[0]):
        c.append(b[0])
        del b[0]

    else:
        c.append(a[0])
        del a[0]

c = c + a + b
print(' '.join(map(str, c)))
