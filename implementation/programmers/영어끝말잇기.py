already = [words[0]]

    for i in range(1, len(words), 1):
        if((words[i] in already) or (words[i - 1][-1] != words[i][0])):
            if((i + 1) % n == 0):
                return (n, (i + 1) // n)
            else:
                return ((i + 1) % n, (i + 1) // n + 1)
        already.append(words[i])

    return [0, 0]
