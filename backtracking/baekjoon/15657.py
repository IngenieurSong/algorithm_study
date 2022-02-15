import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
result = [0]

def bt(height):
    if(height == m):
        print(' '.join(result[1:]))
        return

    for i in board:
        if(int(result[-1]) <= i):
            result.append(str(i))
            bt(height + 1)
            result.pop()

bt(0)
