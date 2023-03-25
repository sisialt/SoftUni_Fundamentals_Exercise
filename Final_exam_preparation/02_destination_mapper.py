import re

line = input()

destinations = []
total_points = 0

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(pattern, line)

for match in matches:
    destination = match.group(2)
    total_points += len(destination)
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")

# (?<=(=|/))[A-Z][a-z][a-z]+(?=\1) => line 13 match.group()
