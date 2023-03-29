s = list(map(str, s))
    stack = ['0', s[0]]

    for i in range(1, len(s), 1):
        if(stack[-1] == s[i]):
            stack.pop()
        else:
            stack.append(s[i])

    return 1 if len(stack) < 2 else 0
