def solution(elements):
    sum_list = set()
    length = len(elements)
    elements = elements + elements[:-1]

    for i in range(1, length + 1, 1):
        for j in range(length):
            sum_list.add(sum(elements[j : j  + i]))

    return len(sum_list)

# 나머지를 이용한 풀이
def solution(elements):
    sum_list = set()

    for i in range(len(elements)):
        sum_list.add(elements[i])
        temp_sum = elements[i]

        for j in range(i + 1, i + len(elements), 1):
            temp_sum += elements[j % len(elements)]
            sum_list.add(temp_sum)

    return len(sum_list)
