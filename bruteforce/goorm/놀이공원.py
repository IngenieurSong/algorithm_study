t = int(input())

def count_trash(x, y, length, graph):
	count = 0
	for i in range(x, x + k, 1):
		for j in range(y, y + k, 1):
			if(graph[i][j] == 1):
				count += 1
	return count

for _ in range(t):
	n, k = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(n)]
	result = float("inf")

	for i in range(n - k + 1):
		for j in range(n - k + 1):
			result = min(result, count_trash(i, j, k, board))

	print(result)
