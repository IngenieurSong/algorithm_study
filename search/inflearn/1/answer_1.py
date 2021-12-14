import sys

# sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    a = str(input())
    a = a.upper()
    for j in range(0, int(len(a)/2) + 1, 1):
        str_leng = int(len(a)) - 1
        if(a[j] != a[str_leng - j]):
            print("#%d NO" %(i + 1))
            break
    if(j == int(len(a)/2)):
        print("#%d YES" %(i + 1))
