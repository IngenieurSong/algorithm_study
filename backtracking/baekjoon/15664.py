import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = ['0'] + []
visited = [0] * (n + 1)
board = sorted(list(map(int, input().split())))
result_dict = {}

def bt(height):
    global n, m

    if(height == m):
        if(result_dict.get(' '.join(result)) == None):
            result_dict[' '.join(result)] = 1
            print(' '.join(result[1 : m + 1]))
        return

    for i in range(n):
            if(not visited[i] and int(result[height]) <= board[i]):
                visited[i] = 1
                result.append(str(board[i]))
                bt(height + 1)
                visited[i] = 0
                result.pop()

bt(0)
