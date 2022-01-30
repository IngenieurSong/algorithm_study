import bisect

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

def count(target, n_list):
    return bisect.bisect_right(n_list, target) - bisect.bisect_left(n_list, target)

for i in m_list:
    print(count(i, n_list), end = " ")
