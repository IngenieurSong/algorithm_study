n = int(input())
roads = list(map(int, input().split()))
board = list(map(int, input().split()))
i = 0
j = 0
answer = 0

while(j < n - 1):
    if(board[i] <= board[j]):
        answer += board[i] * roads[j]
        j += 1
    else:
        i += 1

print(answer)
