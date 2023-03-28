def is_valid_index(idx, text):
    if 0 <= idx < len(text):  # return 0 <= idx < len(text)
        return True
    return False


input_string = input()

while True:
    command = input()
    if command == "Travel":
        break

    command_args = command.split(":")
    action = command_args[0]

    if action == "Add Stop":
        index = int(command_args[1])
        string_to_add = command_args[2]

        if is_valid_index(index, input_string):
            input_string = input_string[:index] + string_to_add + input_string[index:]

    elif action == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])

        if is_valid_index(start_index, input_string) and is_valid_index(end_index, input_string):
            input_string = input_string[:start_index] + input_string[end_index + 1:]

    elif action == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]

        if old_string in input_string:  # without if, .replace() doesnt do anything when no old string
            input_string = input_string.replace(old_string, new_string)

    print(input_string)

print(f"Ready for world tour! Planned stops: {input_string}")
