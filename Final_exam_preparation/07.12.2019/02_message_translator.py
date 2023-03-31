import re

n = int(input())

for _ in range(n):
    line = input()

    pattern = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

    matches = re.findall(pattern, line)  # matches = re.finditer(pattern, line)

    if not matches:  # if not re.match(pattern, line):
        print(f"The message is invalid")
    else:
        for match in matches:
            command = match[0]  # command = match.group(1)
            text = match[1]  # text = match.group(2)

            ascii_numbers = [ord(ch) for ch in text]
            ascii_numbers_as_str = [str(x) for x in ascii_numbers]

            print(f"{command}: {' '.join(ascii_numbers_as_str)}")
