n = int(input())
word = input()

list_of_strings = []
filtered_list = []

for _ in range(n):
    string = input()
    list_of_strings.append(string)
print(list_of_strings)

for el in list_of_strings:
    if word in el:
        filtered_list.append(el)
print(filtered_list)
