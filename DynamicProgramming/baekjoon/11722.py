n = int(input())
board = [0] + list(map(int, input().split()))
cache = [0] * (n + 1)
cache[1] = 1

for i in range(2, n + 1, 1):
    temp_list = [0]
    for j in range(i):
        if(board[i] < board[j]):
            temp_list.append(cache[j])
    cache[i] = max(temp_list)
    cache[i] += 1

print(max(cache))
