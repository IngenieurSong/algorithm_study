import sys
input = sys.stdin.readline

def bt(height):
    if(height == m):
        string = ' '.join(result)

        if string not in dictionary:
            dictionary[string] = 1
            print(string)
        return

    for i in range(n):
        if(visited[i] == 1):
            continue
        result.append(str(board[i]))
        visited[i] = 1
        bt(height + 1)
        result.pop()
        visited[i] = 0

n, m = map(int, input().split())
board = list(map(int, input().split()))
board.sort()
dictionary = {}
result = []
visited = [0] * n
bt(0)
