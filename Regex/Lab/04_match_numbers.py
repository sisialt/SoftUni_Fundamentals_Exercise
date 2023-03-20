import re

line = input()

pattern = r"(^|(?<=\s))\-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, line)

for num in numbers:
    print(num.group(), end=" ")
