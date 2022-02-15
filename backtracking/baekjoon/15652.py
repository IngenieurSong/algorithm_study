import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = [0]

def bt(height):
    if(height == m):
        print(' '.join(result[1:]))
        return

    for i in range(1, n + 1, 1):
        if(int(result[-1]) <= i):
            result.append(str(i))
            bt(height + 1)
            result.pop()

bt(0)
