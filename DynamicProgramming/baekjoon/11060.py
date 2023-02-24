import sys

n = int(input())
jump = list(map(int, sys.stdin.readline().split()))
cache = [n + 1] * n
cache[0] = 0

for i in range(n):
	for j in range(1, jump[i] + 1):
		if i + j < n:
			cache[i + j] = min(cache[i] + 1, cache[i + j])

if cache[n - 1] == n + 1:
	print(-1)
else:
	print(cache[n - 1])
