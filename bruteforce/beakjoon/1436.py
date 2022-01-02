n = int(input())
start_num = 665
count = 0

while(count < n):
    start_num += 1

    if(str(start_num).count("666") > 0):
        count += 1

print(start_num)
