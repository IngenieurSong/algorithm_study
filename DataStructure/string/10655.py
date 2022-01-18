word = str(input())
answer = ""

for i in word:
    if 'a' <= i <= 'z':
        answer += chr((ord(i) + 13) if i <= 'm' else ord(i) - 13)
    elif 'A' <= i <= 'Z':
        answer += chr((ord(i) + 13) if i <= 'M' else ord(i) - 13)
    else:
        answer += i

print(answer)
