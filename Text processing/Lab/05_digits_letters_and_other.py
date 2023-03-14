input_data = input()

digits, letters, other = "", "", ""

for ch in input_data:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch

print(digits)
print(letters)
print(other)
