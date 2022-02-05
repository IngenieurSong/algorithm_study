import math

n, m = map(int, input().split())

top = math.factorial(n)
bottom = math.factorial(n - m) * math.factorial(m)
print(top // bottom)
