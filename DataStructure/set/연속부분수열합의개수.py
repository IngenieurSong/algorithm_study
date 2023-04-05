def solution(elements):
    sum_list = set()
    length = len(elements)
    elements = elements + elements[:-1]

    for i in range(1, length + 1, 1):
        for j in range(length):
            sum_list.add(sum(elements[j : j  + i]))

    return len(sum_list)
