import re

numbers = []

while True:
    text = input()
    if not text:
        break

    pattern = r"\d+"

    res = re.findall(pattern, text)
    numbers.extend(res)

print(" ".join(numbers))
