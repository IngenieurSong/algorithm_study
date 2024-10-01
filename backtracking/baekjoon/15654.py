n, m = map(int, input().split())
result = []
visited = [0] * n
board = sorted(list(map(int, input().split())))

def bt(height):
    global n, m

    if height == m:
        print(' '.join(result))
        return

    for idx, i in enumerate(board):
        if not visited[idx]:
            visited[idx] = 1
            result.append(str(i))
            bt(height + 1)
            visited[idx] = 0
            result.pop()

bt(0)
