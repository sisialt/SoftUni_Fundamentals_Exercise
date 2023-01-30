string = input()
list_from_string = list(string)
list_with_capitals = []

for i in range(0, len(list_from_string)):
    if 65 <= ord(list_from_string[i]) <= 90:
        list_with_capitals.append(i)

print(list_with_capitals)
