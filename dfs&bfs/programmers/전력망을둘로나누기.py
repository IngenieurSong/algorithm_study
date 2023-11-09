from collections import deque

def bfs(board, visit, start):
    queue = deque([start])
    visit[start] = 1
    count = 0

    while(queue):
        node = queue.popleft()
        count += 1

        for i in board[node]:
            if(not visit[i]):
                queue.append(i)
                visit[i] = 1

    return count

def make_tree(i, wires, n):
    board = [[] for _ in range(n + 1)]
    for c in range(len(wires)):
        if(c == i):
            continue
        board[wires[c][0]].append(wires[c][1])
        board[wires[c][1]].append(wires[c][0])

    return board

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        count = []
        board = make_tree(i, wires, n)
        visit = [0] * (n + 1)

        for j in range(1, n + 1, 1):
            if(not visit[j]):
                count.append(bfs(board, visit, j))

        answer = min(answer, abs(count[0] - count[1]))

    return answer
