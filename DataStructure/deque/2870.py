from collections import deque

def check(s):
    queue = deque(list(map(str, s)))
    result = []
    num = ''

    while(queue):
        next = queue.popleft()

        if(next.isdigit()):
            num += next
        elif(num == ''):
            continue
        else:
            result.append(int(num))
            num = ''

    if(num != ''):
        result.append(int(num))

    return result

n = int(input())
result = []
s_list = []

for _ in range(n):
    s_list.append(str(input()))

for i in s_list:  
    result.extend(check(i))

for i in sorted(result):
    print(i)
