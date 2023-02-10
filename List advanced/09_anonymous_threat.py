input_data = input(). split()

command = input()

new_list = []
merge_counter = 0

while command != "3:1":
    action, first_arg, second_arg = command.split()
    first_arg = int(first_arg)
    second_arg = int(second_arg)
    result_from_merge = ""

    if action == "merge":

        if first_arg < 0:
            first_arg = 0

        if merge_counter == 0:
            if second_arg > len(input_data):
                second_arg = len(input_data)
                first_arg -= second_arg
                if first_arg < 0:
                    first_arg = 0
        else:
            if second_arg > len(new_list):
                first_arg -= (second_arg - len(new_list) + 1)
                if first_arg < 0:
                    first_arg = 0
                second_arg = len(new_list) - 1

        for i in range(first_arg, second_arg + 1):
            if merge_counter == 0:
                result_from_merge += input_data[i]
            else:
                result_from_merge += new_list[i]

        if second_arg - first_arg < len(input_data):
            if merge_counter != 0:
                input_data = new_list.copy()
            new_list.clear()
            new_list.insert(first_arg, result_from_merge)
            new_list.insert(first_arg + 1, "".join(input_data[second_arg + 1:]))

        merge_counter += 1

    command = input()

print(new_list)
print((" ".join(new_list)).strip())

    # elif action == "divide":
    #     pass
    #
    #
    # command = input()
