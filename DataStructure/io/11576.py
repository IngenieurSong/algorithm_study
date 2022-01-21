import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
number = list(map(int, input().split()))
board = [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
sum = 0
answer = []

for i in range(n):
    sum += number[-1 - i] * (a ** i)

while(sum):
    answer.append(sum % b)
    sum = sum // b

for i in range(len(answer)):
    print(answer[-1 - i], end = " ")
