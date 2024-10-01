def solution(n, tops):
    prev2, prev1 = 1, 1
    
    for i in range(2, 2 * n + 2, 1):
        if i % 2 == 0 and tops[i // 2 - 1] == 1:
            current = prev1 * 2 + prev2
        else:
            current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1 % 10007
