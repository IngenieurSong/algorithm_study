import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
visited = [0] * 10001
result = []

def bt(height):
    global n, m

    if(height == m):
        print(' '.join(result))
        return

    for i in board:
        if(visited[i] == 0):
            visited[i] = 1
            result.append(str(i))
            bt(height + 1)
            visited[i] = 0
            result.pop()

bt(0)
