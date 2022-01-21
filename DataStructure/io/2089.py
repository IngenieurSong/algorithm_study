import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
answer = ""

while (n):
    if (n % (-2)):
        answer += "1"
        n = n // (-2) + 1
    else:
        answer += "0"
        n = n // (-2)

print(answer[::-1] if answer else "0")
