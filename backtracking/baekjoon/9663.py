def n_queens(x):
    global n, count

    if(x == n):
        count += 1
        return

    for i in range(n):
        col[x] = i
        if(promising(x)):
            n_queens(x + 1)

def promising(x):
    for j in range(x):
        if(col[j] == col[x] or abs(col[j] - col[x]) == (x - j)):
            return 0
    return 1

n = int(input())
col = [0] * n
count = 0
n_queens(0)
print(count)
