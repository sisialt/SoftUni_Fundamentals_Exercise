number = input()

number_as_list = list(number)
the_largest = []

for i in range(len(number)):
    the_largest.append(max(number_as_list))
    number_as_list.remove(max(number_as_list))

print("".join(the_largest))

# num = input()
# number = int("".join(sorted(str(num), reverse=True)))
# print(number)

