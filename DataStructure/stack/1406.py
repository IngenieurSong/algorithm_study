import sys
from collections import deque

input = sys.stdin.readline
word = list(input().strip())
temp = []
n = int(input())

def l():
    if(word):
        temp.append(word.pop())

def d():
    if(temp):
        word.append(temp.pop())

def b():
    if(word):
        word.pop()

def p(element):
    word.append(element)

for _ in range(n):
    command = list(map(str, input().split()))

    if(command[0] == "P"):
        p(command[1])
    elif(command[0] == "L"):
        l()
    elif(command[0] == "B"):
        b()
    elif(command[0] == "D"):
        d()

print("".join(word + list(reversed(temp))))
