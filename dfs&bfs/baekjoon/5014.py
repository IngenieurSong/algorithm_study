from collections import deque

f, s, g, u, d = map(int, input().split())
cache = [float("inf")] * (f + 1)
vector = [u, -d]
cache[s] = 0

def bfs(cache, start):
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for move in vector:
            new_node = node + move

            if(new_node < 1 or new_node > f):
                continue
            if(cache[new_node] == float("inf")):
                cache[new_node] = min(cache[new_node], cache[node] + 1)
                queue.append(new_node)

bfs(cache, s)
print(cache[g] if cache[g] != float("inf") else "use the stairs")
