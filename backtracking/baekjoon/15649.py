import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n + 1)
result = []

def bt(height):
    global n, m

    if(height == m):
        print(' '.join(result))
        return

    for i in range(1, n + 1, 1):
        if(visited[i] == 0):
            visited[i] = 1
            result.append(str(i))
            bt(height + 1)
            visited[i] = 0
            result.pop()

bt(0)
