import sys
input = sys.stdin.readline

def bt(height):
    if(height == m):
        string = ' '.join(result[1:])

        if string not in dictionary:
            dictionary[string] = 1
            print(string)
        return

    for i in range(n):
        if(visited[i] == 0 and int(result[-1]) <= board[i]):
            result.append(str(board[i]))
            visited[i] = 1
            bt(height + 1)
            result.pop()
            visited[i] = 0

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
dictionary = {}
result = [0]
visited = [0] * n
bt(0)
