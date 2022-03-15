from collections import deque

n, k = map(int, input().split())
board = [0] * 100001

def bfs(start):
    queue = deque([])
    queue.append(start)

    while(queue):
        node = queue.popleft()

        if(node == k):
            break

        for i in [node + 1, node - 1, 2 * node]:
            if(0 <= i <= 100000 and not board[i]):
                board[i] = board[node] + 1
                queue.append(i)

bfs(n)
print(board[k])
