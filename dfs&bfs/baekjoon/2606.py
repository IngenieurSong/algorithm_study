n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

root_of_1 = find_parent(parent, 1)
infected_computers = 0

# 각 컴퓨터가 1번 컴퓨터와 같은 부모를 가지는지 확인
for i in range(2, n + 1):  # 1번 컴퓨터는 제외하고 카운트
    if find_parent(parent, i) == root_of_1:
        infected_computers += 1

print(infected_computers)
