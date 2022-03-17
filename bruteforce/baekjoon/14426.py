import sys
input = sys.stdin.readline

n, m = map(int, input().split())
strings = {input().strip() for _ in range(n)}
count = 0

for _ in range(m):
    pattern = input().strip()
    for s in strings:
        if s.startswith(pattern):
            count += 1
            break
print(count)
