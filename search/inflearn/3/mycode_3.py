import sys

# sys.stdin = open("input.txt", "r")
card = [number for number in range(1, 21, 1)]

for i in range(10):
    n1, n2 = map(int, input().split(" "))

    for j in range(n1 - 1, (n1 + n2) // 2, 1):
        temp = card[j]
        card[j] = card[n1 + n2 - 2 - j]
        card[n1 + n2 - 2 - j] = temp

print(' '.join(map(str, card)))
