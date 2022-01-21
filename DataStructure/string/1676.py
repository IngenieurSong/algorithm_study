import sys
input = sys.stdin.readline

n = int(input())
result = 1
count = 0

for i in range(1, n + 1, 1):
    result *= i

result = str(result)

for i in range(len(str(result))):
    if(result[-1 - i] != "0"):
        break
    else:
        count += 1

print(count)
