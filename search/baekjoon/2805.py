import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 1
end = max(height)

while(start <= end):
    length = 0
    mid = (start + end) // 2

    for i in height:
        if(i > mid):
            length += i - mid

    if(length >= m):
        start = mid + 1
    else:
        end = mid - 1

print(str(end))
