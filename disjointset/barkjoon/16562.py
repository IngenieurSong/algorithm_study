import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())
parent = [i for i in range(n + 1)]
board = [0] + list(map(int, input().split()))
price = 0
visited = [0] * (n + 1)

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])

    return parent[node]

def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if(board[a] < board[b]):
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a, b, parent)

for i in range(1, n + 1, 1):
    find_parent(parent, i)

for i in range(1, n + 1, 1):
    if (parent.count(i) and visited[i] == 0):
        visited[i] = 1
        price += board[i]

if(price > k):
    print("Oh no")
else:
    print(price)
