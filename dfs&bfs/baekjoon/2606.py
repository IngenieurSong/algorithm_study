import sys
sys.setrecursionlimit(5000)

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

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

for i in range(1, n + 1, 1):
    find_parent(parent, i)

print(parent.count(1) - 1)
