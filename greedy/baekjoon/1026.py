 = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0

a = sorted(a)
b = sorted(b, reverse = True)
for i in range(n):
    s += a[i] * b[i]

print(s)
