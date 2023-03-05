input_data = input().split()
input_data = "".join(input_data)

count_chars = {}

for el in input_data:
    if el not in count_chars:
        count_chars[el] = 1
    else:
        count_chars[el] += 1

for char, occurrences in count_chars.items():
    print(f"{char} -> {occurrences}")
