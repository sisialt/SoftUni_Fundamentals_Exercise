first_char_index = int(input())
second_char_index = int(input())

for char in range(first_char_index, second_char_index + 1):
    print(chr(char), end=" ")
