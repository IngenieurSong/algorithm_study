import sys

# sys.stdin = open("input.txt", "r")
n = input()
num_list = []
z = 0
count = 0

for i in n:
    if(i.isdecimal()):
        z = z*10 + int(i)

print(z)

for i in range(1, z + 1, 1):
    if(z % i == 0):
        count += 1

print(count)
