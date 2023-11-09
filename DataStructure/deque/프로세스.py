from collections import deque

def solution(priorities, location):
    task = [i for i in enumerate(priorities)]
    queue = deque(task)
    done = []

    while(queue):
        current = queue.popleft()

        for p in queue:
            if(current[1] < p[1]):
                queue.append(current)
                break
        else:
            done.append(current[0])

    answer = done.index(location) + 1
    return answer
