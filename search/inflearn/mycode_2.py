import sys

# sys.stdin = open("input.txt", "r")
n = input()
num_list = []
z = 0

for i in n:
    if(i.isdigit()):
        num_list.append(i)

number = int(''.join(num_list))
print(number)

for i in range(1, number + 1, 1):
    if(number % i == 0):
        z += 1

print(z)
