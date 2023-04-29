n = int(input())
word = input()

list_of_strings = []
filtered_list = []

for _ in range(n):
    string = input()
    list_of_strings.append(string)
    if word in string:
        filtered_list.append(string)

print(list_of_strings)
print(filtered_list)