n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
count = 0
comp = 0

table = sorted(table, key = lambda x: (x[1], x[0]))

for i in table:
    if(i[0] >= comp):
        count += 1
        comp = i[i]

print(count)
