from collections import deque

def check(skill, skill_tree):
    skill_queue = deque(list(map(str, skill)))
    for c in skill_tree:
        if(c not in skill):
            continue
        if(c != skill_queue[0]):
            return False
        else:
            skill_queue.popleft()
    return True

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        if(check(skill, skill_tree)):
            answer += 1

    return answer
