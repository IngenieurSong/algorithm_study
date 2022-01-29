k, n = map(int, input().split())
wire = []

for _ in range(k):
    wire.append(int(input()))

start = 1
end = max(wire)

while(start <= end):
    count = 0
    mid = (start + end) // 2

    for i in wire:
        count += i // mid

    if(count >= n):
        start = mid + 1
    else:
        end = mid - 1
 
print(end)
