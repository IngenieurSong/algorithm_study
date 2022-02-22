import itertools

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
food = float("inf")
comb = []

for i in range(1, n + 1, 1):
    comb.append(list(itertools.combinations(board, i)))

for i in comb:
    for j in i:
        comp_s = 1
        comp_b = 0
        for k in j:
            comp_s *= k[0]
            comp_b += k[1]

        food = min(food, abs(comp_s - comp_b))

print(food)
