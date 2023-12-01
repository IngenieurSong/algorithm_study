from collections import deque

def check(board):
    queue = deque([board[0]])

    for i in range(1, len(board), 1):
        if(not queue):
            queue.append(board[i])
            continue

        if(board[i] == ')' and queue[0] == '('):
            queue.popleft()
        else:
            queue.append(board[i])

    return "YES" if not queue else "NO"

t = int(input())

for _ in range(t):
    board = list(map(str, input()))

    result = check(board)
    print(result)
