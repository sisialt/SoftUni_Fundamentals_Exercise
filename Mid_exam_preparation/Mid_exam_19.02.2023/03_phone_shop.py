def is_in_sequence(seq, sequence):
    if seq in sequence:
        return True
    return False


phones = input().split(", ")
command = input()

while command != "End":
    command_args = command.split(" - ")
    action = command_args[0]

    if action == "Add":
        phone = command_args[1]
        if not is_in_sequence(phone, phones):
            phones.append(phone)

    elif action == "Remove":
        phone = command_args[1]
        if is_in_sequence(phone, phones):
            phones.remove(phone)

    elif action == "Bonus phone":
        old_phone = command_args[1].split(":")[0]
        new_phone = command_args[1].split(":")[1]
        if is_in_sequence(old_phone, phones):
            phones.insert(phones.index(old_phone) + 1, new_phone)

    elif action == "Last":
        phone = command_args[1]
        if is_in_sequence(phone, phones):
            phones.remove(phone)
            phones.append(phone)

    command = input()

print(*phones, sep=", ")
