n = list(map(int, input()))

n.sort(reverse = True)
if(n[-1] != 0 or sum(n) % 3 != 0):
    print(-1)
else:
    for i in n:
        print(i, end = "")
