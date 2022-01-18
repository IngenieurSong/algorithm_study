import sys
input = sys.stdin.readline

word = str(input())
cache = [i for i in "abcdefghijklmnopqrstuvwxyz"]

for i in range(len(cache)):
    cache[i] = word.find(cache[i])

for i in cache:
    print(i, end = " ")
