def solution(board):
    answer = 0
    n = len(board[0])
    vector = [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

    for i in range(n):
        for j in range(n):
            if(board[i][j] == 1):
                answer += 1
                for nx, ny in vector:
                    nx = i + nx
                    ny = j + ny

                    if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                        continue
                    if(board[nx][ny] == 0):
                        board[nx][ny] = 2
                        answer += 1
    
    return (n ** 2) - answer
