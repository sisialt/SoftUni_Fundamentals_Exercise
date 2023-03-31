string = input()

while True:
    line = input()
    if line == "Finish":
        break

    line_args = line.split()
    command = line_args[0]

    if command == "Replace":
        current_char = line_args[1]
        new_char = line_args[2]

        string = string.replace(current_char, new_char)
        print(string)

    elif command == "Cut":
        start_index = int(line_args[1])
        end_index = int(line_args[2])

        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
            print(string)
        else:
            print("Invalid indexes!")

    elif command == "Make":
        upper_or_lower = line_args[1]
        if upper_or_lower == "Upper":
            string = string.upper()
        elif upper_or_lower == "Lower":
            string = string.lower()
        print(string)

    elif command == "Check":
        substring = line_args[1]

        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif command == "Sum":
        start_index = int(line_args[1])
        end_index = int(line_args[2])

        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            substring = string[start_index:end_index + 1]
            sum_ascii_substring = sum([ord(ch) for ch in substring])
            print(sum_ascii_substring)
        else:
            print("Invalid indexes!")



