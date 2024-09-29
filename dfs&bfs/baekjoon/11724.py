import sys

input = sys.stdin.readline

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]

def union_parent(parent, node1, node2):
    parent1 = find_parent(parent, node1)
    parent2 = find_parent(parent, node2)

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

for i in range(n + 1):
    find_parent(parent, i)

print(len(set(parent)) - 1)
