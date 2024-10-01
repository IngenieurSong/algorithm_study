n, m = map(int, input().split())
result = []

def bt(height):
    global n, m

    if height == m:
        print(' '.join(result))
        return

    for i in range(1, n + 1, 1):
        result.append(str(i))
        bt(height + 1)
        result.pop()

bt(0)
