n = int(input())

for _ in range(n):
    board = list(map(str, input()))
    sum = 0

    for i in board:
        if(sum == -1):
            break

        else:
            if(i == "("):
                sum += 1
            else:
                sum -= 1

    if(sum == 0):
        print("YES")
    else:
        print("NO")
