import re

persons_info = []

while True:
    line = input()
    if line == "make migrations":
        break

    pattern = r"(?<=name is )([A-Z][a-z]+ [A-Z][a-z]+).* (\d{2}) years.*on (\d{2}\-\d{2}\-\d{4})\."

    matches = re.findall(pattern, line)

    if not matches:
        continue

    for match in matches:
        persons_info.append([match[0], match[1], match[2]])

if not persons_info:
    print("DB is empty")
else:
    for person_info in persons_info:
        print(f"Name of the person: {person_info[0]}.")
        print(f"Age of the person: {int(person_info[1])}.")
        print(f"Birthdate of the person: {person_info[2]}.")
