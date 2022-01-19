from collections import deque

n, k = map(int, input().split())

board = deque([str(i) for i in range(1, n + 1, 1)])
answer = []

while(board):
    board.rotate(-(k - 1))
    answer.append(board.popleft())

print("<" + ", ".join(answer) + ">")
