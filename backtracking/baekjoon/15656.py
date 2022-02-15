import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
result = []

def bt(height):
    if(height == m):
        print(' '.join(result))
        return

    for i in board:
        result.append(str(i))
        bt(height + 1)
        result.pop()
 
bt(0)
