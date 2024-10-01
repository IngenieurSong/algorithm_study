n, m = map(int, input().split())
result = []
board = sorted(list(map(int, input().split())))

def bt(height):
    global n, m

    if height == m:
        print(' '.join(result))
        return

    for idx, i in enumerate(board):
        if i > (int(result[-1]) if result else 0):
            result.append(str(i))
            bt(height + 1)
            result.pop()

bt(0)
