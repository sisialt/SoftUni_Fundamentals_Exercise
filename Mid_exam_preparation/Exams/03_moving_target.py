def is_valid_index(idx, sequence):
    if 0 <= idx < len(sequence):
        return True
    return False


targets = [int(x) for x in input().split()]
command = input()

while command != "End":

    action = command.split()[0]
    index = int(command.split()[1])

    if action == "Shoot":
        power = int(command.split()[2])
        if is_valid_index(index, targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        value = int(command.split()[2])
        if is_valid_index(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(command.split()[2])
        if not is_valid_index(index - radius, targets) or not is_valid_index(index + radius, targets):
            print("Strike missed!")
        else:
            for i in range(radius * 2 + 1):
                targets.remove(targets[index - radius])

    command = input()

else:
    print("|".join([str(x) for x in targets]))
