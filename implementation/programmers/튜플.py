def str_to_list(s):
    board = []
    s = s[2:-2].split("},{")

    for i in s:
        board.append(list(map(int, i.split(','))))

    return board

def solution(s):
    answer = []
    board = str_to_list(s)
    board.sort(key = lambda x : len(x))

    for target in board:
        for t in target:
            if(t not in answer):
                answer.append(t)

    return answer
