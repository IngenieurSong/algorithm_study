def solution(n):
    answer = 0
    board = [i for i in range(n + 1)]

    for i in range(2, n + 1, 1):
        for j in range(i, n + 1, i):
            if(board[j] and j != i):
                answer += 1
                board[j] = 0

    return answer
