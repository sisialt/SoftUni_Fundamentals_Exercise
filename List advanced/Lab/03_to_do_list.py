notes = [""] * 10

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split("-")

    importance = int(line_args[0]) - 1
    note = line_args[1]

    notes.pop(importance)
    notes.insert(importance, note)

print(f"{[el for el in notes if el != '']}")
