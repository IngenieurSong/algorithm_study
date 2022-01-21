n = int(input())
m = 2

while(n != 1):
    if(n % m == 0):
        n = n // m
        print(m)
    else:
        m += 1
