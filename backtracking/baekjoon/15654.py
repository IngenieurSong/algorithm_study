import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * n
result = []
board = sorted(list(map(int, input().split())))

def bt(height):
    global n, m

    if(height == m):
        print(' '.join(result))
        return

    for i in range(n):
        if(not visited[i]):
            visited[i] = 1
            result.append(str(board[i]))
            bt(height + 1)
            visited[i] = 0
            result.pop()

bt(0)
