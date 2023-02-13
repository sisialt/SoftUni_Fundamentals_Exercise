input_data = input(). split()
command = input()

while command != "3:1":
    action, first_arg, second_arg = command.split()
    first_arg = int(first_arg)
    second_arg = int(second_arg)

    result_from_merge = ""
    result_from_divide = []

    if action == "merge":

        first_arg = max(0, first_arg)
        second_arg = min(len(input_data) - 1, second_arg)

        for i in range(first_arg, second_arg + 1):
            result_from_merge += input_data[i]

        for _ in range(second_arg - first_arg + 1):
            input_data.pop(first_arg)

        input_data.insert(first_arg, result_from_merge)

    elif action == "divide":

        chars_in_divided_part = len(input_data[first_arg]) // second_arg
        word_to_divide = input_data[first_arg]

        for n in range(0, second_arg * 2, 2):
            divided_part = ""
            for i in range(0 + n, chars_in_divided_part + n):
                divided_part += word_to_divide[i]
            result_from_divide.append(divided_part)

        input_data.pop(first_arg)

        for i in range(second_arg):
            input_data.insert(first_arg + i, result_from_divide[i])

    command = input()

print(" ".join(input_data))

