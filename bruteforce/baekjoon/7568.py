n = int(input())
dc_list = [list(map(int, input().split())) for _ in range(n)]
price_list = []

for i in range(n):
    price = 1
    for j in range(n):
        if(dc_list[i][0] < dc_list[j][0] and dc_list[i][1] < dc_list[j][1]):
            price += 1
    price_list.append(price)

for i in price_list:
    print(i)
