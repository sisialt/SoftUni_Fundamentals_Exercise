import re

line = input()

pattern = r"(?P<Day>\d{2})(?P<sep>\.|\-|/)(?P<Month>[A-Z][a-z]{2})(?P=sep)(?P<Year>\d{4})"

results = re.finditer(pattern, line)
for res in results:
    date = res.groupdict()
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")
