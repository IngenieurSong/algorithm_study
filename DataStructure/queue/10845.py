from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

def push(element):
    queue.append(element)

def pop():
    if(not queue):
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if(not queue):
        print(1)
    else:
        print(0)

def front():
    if(not queue):
        print(-1)
    else:
        print(queue[0])

def back():
    if(not queue):
        print(-1)
    else:
        print(queue[-1])

for _ in range(n):
    command = list(map(str, input().split()))

    if(command[0] == "push"):
        push(command[1])
    elif(command[0] == "pop"):
        pop()
    elif(command[0] == "size"):
        size()
    elif(command[0] == "empty"):
        empty()
    elif(command[0] == "front"):
        front()
    elif(command[0] == "back"):
        back()
