n, m = map(int, input().split())
result = []
board = sorted(list(map(int, input().split())))

def bt(height):
    global n, m

    if height == m:
        print(' '.join(result))
        return

    for idx, i in enumerate(board):
        result.append(str(i))
        bt(height + 1)
        result.pop()

bt(0)
