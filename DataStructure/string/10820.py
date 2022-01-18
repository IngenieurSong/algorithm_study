while(True):
    l = 0
    u = 0
    s = 0
    n = 0
    word = sys.stdin.readline().rstrip("\n")
    if(not word):
        break

    for i in word:
        if(i.islower()):
            l += 1
        elif(i.isupper()):
            u += 1
        elif(i.isspace()):
            s += 1
        elif(i.isdigit()):
            n += 1

    print(l, u, n, s)
