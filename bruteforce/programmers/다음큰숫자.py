condition_2 = list(map(str, str(bin(n)))).count('1')
    m = n + 1

    while True:
        if(list(map(str, str(bin(m)))).count('1') == condition_2):
            return m
        m += 1
