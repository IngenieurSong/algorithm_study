import sys
input = sys.stdin.readline

n = int(input())
stack = []

def push(element):
    stack.append(element)

def size():
    print(len(stack))

def top():
    if(not stack):
        print(-1)
    else:
        print(stack[-1])

def empty():
    if(not stack):
        print(1)
    else:
        print(0)

def pop():
    if(not stack):
        print(-1)
    else:
        print(stack.pop())

for _ in range(n):
    command = list(map(str, input().split()))

    if(command[0] == "push"):
        push(command[1])

    elif(command[0] == "size"):
        size()

    elif(command[0] == "top"):
        top()

    elif(command[0] == "empty"):
        empty()

    elif(command[0] == "pop"):
        pop()
