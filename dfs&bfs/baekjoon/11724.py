import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if(parent[x] != x):
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

for i in range(n + 1):
    find_parent(parent, i)

print(len(set(parent)) - 1)
