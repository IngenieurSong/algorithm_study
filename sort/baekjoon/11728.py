n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))
result = []
idx_n = 0
idx_m = 0

while(True):
    if(n_list[idx_n] > m_list[idx_m]):
        result.append(m_list[idx_m])
        idx_m += 1
    else:
        result.append(n_list[idx_n])
        idx_n += 1

    if(idx_n == len(n_list)):
        result = result + m_list[idx_m:]
        break
    elif(idx_m == len(m_list)):
        result = result + n_list[idx_n:]
        break

for i in result:
    print(i, end = " ")
