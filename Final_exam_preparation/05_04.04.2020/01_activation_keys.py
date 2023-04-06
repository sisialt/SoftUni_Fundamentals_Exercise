activation_key = input()

while True:
    line = input()
    if line == "Generate":
        break

    line_args = line.split(">>>")
    command = line_args[0]

    if command == "Contains":
        substring = line_args[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        upper_or_lower = line_args[1]
        start_index = int(line_args[2])
        end_index = int(line_args[3])

        substring_to_change = activation_key[start_index:end_index]

        if upper_or_lower == "Upper":
            substring_to_change = substring_to_change.upper()
            activation_key = activation_key[:start_index] + substring_to_change + activation_key[end_index:]
        elif upper_or_lower == "Lower":
            substring_to_change = substring_to_change.lower()
            activation_key = activation_key[:start_index] + substring_to_change + activation_key[end_index:]

        print(activation_key)

    elif command == "Slice":
        start_index = int(line_args[1])
        end_index = int(line_args[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
