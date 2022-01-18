word = str(input())
word_list = [word[i:] for i in range(len(word))]

word_list.sort()
for i in word_list:
    print(i)
