import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n + 1)
result = ['0'] + []

def bt(height):
    global n, m

    if(height == m):
        print(' '.join(result[1 : m + 1]))
        return

    for i in range(1, n + 1, 1):
            if(int(result[height]) <= i):
                result.append(str(i))
                bt(height + 1)
                result.pop()

bt(0)
