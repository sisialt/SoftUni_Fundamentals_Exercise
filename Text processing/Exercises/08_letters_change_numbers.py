# A12b s17G
from string import ascii_lowercase

strings = [string.strip() for string in input().split()]

total_sum = 0

for string in strings:
    first_letter = string[0]
    number = int(string[1:-1])
    last_letter = string[-1]

    result = 0
    first_letter_position_in_alphabet = ord(first_letter.upper()) - 64  # ascii_lowercase.index(first_letter.lower()) + 1
    last_letter_position_in_alphabet = ord(last_letter.upper()) - 64
    if first_letter.isupper():
        result = number / first_letter_position_in_alphabet
    else:
        result = number * first_letter_position_in_alphabet

    if last_letter.isupper():
        result -= last_letter_position_in_alphabet
    else:
        result += last_letter_position_in_alphabet

    total_sum += result

print(f"{total_sum:.2f}")
