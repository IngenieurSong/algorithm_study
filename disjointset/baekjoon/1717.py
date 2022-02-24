import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] + [i for i in range(1, n + 1, 1)]

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

for _ in range(m):
    command, a, b = map(int, input().split())

    if(command == 1):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if(a == b):
            print("YES")
        else:
            print("NO")

    elif(command == 0):
        union_parent(parent, a, b)
