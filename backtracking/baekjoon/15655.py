import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
visited = [0] * 10001
result = [0]

def bt(height):
    global n, m

    if(height == m):
        print(' '.join(result[1:]))
        return

    for i in board:
        if(visited[i] == 0 and int(result[-1]) < i):
            visited[i] = 1
            result.append(str(i))
            bt(height + 1)
            visited[i] = 0
            result.pop()

bt(0)
