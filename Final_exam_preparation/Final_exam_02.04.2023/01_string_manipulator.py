text = input()

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split()
    command = line_args[0]

    if command == "Translate":
        char = line_args[1]
        replacement = line_args[2]
        text = text.replace(char, replacement)
        print(text)

    elif command == "Includes":
        substring = line_args[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif command == "Start":
        substring = line_args[1]
        if text.startswith(substring):
            print("True")
        else:
            print("False")

    elif command == "Lowercase":
        text = text.lower()
        print(text)

    elif command == "FindIndex":
        char = line_args[1]
        for i in range(-1, -len(text), -1):
            if text[i] == char:
                print(f"{len(text) + i}")
                break

    elif command == "Remove":
        start_idx = int(line_args[1])
        count = int(line_args[2])
        text = text[:start_idx] + text[start_idx + count:]
        print(text)

