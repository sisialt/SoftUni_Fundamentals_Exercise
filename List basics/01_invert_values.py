string = input()
list_of_string = string.split()
list_of_string_opposite = []

for el in list_of_string:
    el = int(el)
    list_of_string_opposite.append(-el)

print(list_of_string_opposite)
    