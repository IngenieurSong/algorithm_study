import sys
input = sys.stdin.readline

x, n = map(int, input().split())
board = [0] + list(map(int, input().split()))

if(max(board) == 0):
    print("SAD")
else:
    prefix = [0]

    for i in range(1, x + 1, 1):
        prefix.append(prefix[i - 1] + board[i])

    start = 0
    end = n
    max_sum = 0
    count = 0

    while(end < x + 1):
        if(max_sum < prefix[end] - prefix[start]):
            max_sum = prefix[end] - prefix[start]
            count = 1
        elif(max_sum == prefix[end] - prefix[start]):
            count += 1

        start += 1
        end += 1

    print(max_sum)
    print(count)
