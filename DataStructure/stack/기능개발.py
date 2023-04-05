def solution(progresses, speeds):
    answer = []
    remain = []

    for i in range(len(progresses)):
        q, r = divmod(100 - progresses[i], speeds[i])
        if(r):
            remain.append(q + 1)
        else:
            remain.append(q)

    stack = [remain[0]]

    for i in range(1, len(remain), 1):
        if(stack[0] < remain[i]):
            answer.append(len(stack))
            stack = [remain[i]]
        else:
            stack.append(remain[i])

    answer.append(len(stack))

    return answer
