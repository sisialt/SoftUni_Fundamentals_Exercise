words = input().lower().split(" ")

word_and_occurrences = {}

for word in words:
    if word not in word_and_occurrences:
        word_and_occurrences[word] = 1
    else:
        word_and_occurrences[word] += 1

for word, occurrences in word_and_occurrences.items():
    if occurrences % 2 == 1:
        print(word, end=" ")
