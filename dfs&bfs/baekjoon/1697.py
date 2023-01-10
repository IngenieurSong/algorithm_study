from collections import deque

n, k = map(int, input().split())
cache = [0] * 100001

def bfs(start):
    queue = deque([start])
    cache[start] = 1

    while queue:
        node = queue.popleft()

        if(node == k):
            break

        for i in [node + 1, node - 1, node * 2]:
            if(i >= 0 and i <= 100000 and not cache[i]):
                queue.append(i)
                cache[i] = cache[node] + 1

bfs(n)
print(cache[k] - 1)
