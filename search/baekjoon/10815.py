n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))
count = 0

def binary_search(target, start, end, n_list):
    while(start <= end):
        mid = (start + end) // 2

        if(n_list[mid] > target):
            end = mid - 1
        elif(n_list[mid] < target):
            start = mid + 1
        elif(n_list[mid] == target):
            return 1

    return 0

for i in m_list:
    print(binary_search(i, 0, len(n_list) - 1, n_list), end = " ")
