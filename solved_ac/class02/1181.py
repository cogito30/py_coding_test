# 단어 정렬
N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input())

word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)