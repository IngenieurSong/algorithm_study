n, m = map(int, input().split())
result = []
visited = [0] * (n + 1)

def bt(height):
    global n, m

    if height == m:
        print(' '.join(result))
        return

    for i in range(1, n + 1, 1):
        if not visited[i]:
            visited[i] = 1
            result.append(str(i))
            bt(height + 1)
            visited[i] = 0
            result.pop()

bt(0)
