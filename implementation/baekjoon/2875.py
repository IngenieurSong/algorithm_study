n, m, k = map(int, input().split())

count = 0

while(m + n >= k and n >= 0 and m >= 0):
    n -= 2
    m -= 1
    count += 1

print(count - 1)
