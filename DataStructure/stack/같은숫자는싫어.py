def solution(arr):
    stack = [arr[0]]

    for i in range(1, len(arr), 1):
        if(stack[-1] != arr[i]): # 연속되는 같은 숫자가 아닌 경우만 stack에 추가함
            stack.append(arr[i])
    return stack
