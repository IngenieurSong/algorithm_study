import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent, node):
    if(parent[node] != node):
        parent[node] = find_parent(parent, parent[node])

    return parent[node]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] + [i for i in range(1, n + 1, 1)]

for i in range(1, n + 1, 1):
    edge = [0] + list(map(int, input().split()))

    for j in range(1, n + 1, 1):
        if(edge[j] == 1):
            union_parent(parent, i, j)

board = list(map(int, input().split()))

for i in range(m - 1):
    a = find_parent(parent, board[i])
    b = find_parent(parent, board[i + 1])

    if(a != b):
        print("NO")
        break
else:
    print("YES")
