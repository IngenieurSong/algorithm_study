n = int(input())
m = int(input())
if(m > 0):
    button = list(map(int, input().split()))
else:
    button = []

def check(k):
    for j in str(k):
        if(int(j) in button):
            return False
    return True

result = abs(n - 100)
for i in range(1000001):
    if(check(i)):
        result = min(result, len(str(i)) + abs(i - n))

print(result)
