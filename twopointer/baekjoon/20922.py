n, k = map(int, input().split())
board = list(map(int, input().split()))
cache = [0] * (max(board) + 1)
start = 0
end = 0
max_num = 0

while(end < n):
    if(cache[board[end]] < k):
        cache[board[end]] += 1
        end += 1
    else:
        cache[board[start]] -= 1
        start += 1

    max_num = max(max_num, end - start)

print(max_num)
