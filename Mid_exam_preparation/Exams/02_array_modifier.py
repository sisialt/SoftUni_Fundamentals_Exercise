array = [int(x) for x in input().split()]
command = input()

while command != "end":
    command_args = command.split()
    action = command_args[0]

    if action == "swap":
        index1, index2 = int(command_args[1]), int(command_args[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif action == "multiply":
        index1, index2 = int(command_args[1]), int(command_args[2])
        array[index1] = array[index1] * array[index2]

    elif action == "decrease":
        for i in range(len(array)):
            array[i] -= 1

    command = input()

print(*array, sep=", ")
