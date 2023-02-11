input_data = input(). split()

command = input()

new_list = []

while command != "3:1":
    action, first_arg, second_arg = command.split()
    first_arg = int(first_arg)
    second_arg = int(second_arg)

    result_from_merge = ""
    result_from_divide = []

    if action == "merge":

        first_arg = max(0, first_arg)
        second_arg = min(len(input_data) - 1, second_arg)
        difference = second_arg - first_arg

        if first_arg >= second_arg:
            first_arg = second_arg - difference

        for i in range(first_arg, second_arg + 1):
            result_from_merge += input_data[i]

        for _ in range(difference + 1):
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

# while command != "3:1":
#     action, first_arg, second_arg = command.split()
#     first_arg = int(first_arg)
#     second_arg = int(second_arg)
#
#     result_from_merge = ""
#     result_from_divide = ""
#
#     if action == "merge":
#
#         if first_arg < 0:
#             first_arg = 0
#
#         if merge_counter == 0:
#             if second_arg > len(input_data):
#                 second_arg = len(input_data) - 1
#                 if not 0 <= first_arg < len(input_data):
#                     first_arg -= second_arg
#                     if first_arg < 0:
#                         first_arg = 0
#         else:
#             if second_arg > len(new_list):
#                 second_arg = len(new_list)
#                 second_arg -= 1
#                 if not 0 <= first_arg < len(new_list):
#                     first_arg -= second_arg
#                     if first_arg < 0:
#                         first_arg = 0
#
#
#         for i in range(first_arg, second_arg + 1):
#             if merge_counter == 0:
#                 result_from_merge += input_data[i]
#             else:
#                 result_from_merge += new_list[i]
#
#         if second_arg - first_arg < len(input_data):
#             if merge_counter != 0:
#                 input_data = new_list.copy()
#             new_list.clear()
#             new_list.insert(first_arg - 1, "".join(input_data[:first_arg]))
#             new_list.insert(first_arg, result_from_merge)
#             new_list.insert(first_arg + 1, "".join(input_data[second_arg + 1:]))
#
#         merge_counter += 1
#
#     elif action == "divide":
#         if merge_counter == 0 and divide_counter == 0:
#             if len(input_data[first_arg]) % second_arg == 0:
#                 chars_to_divide_in_to = len(input_data[first_arg]) / second_arg
#                 for i in range(0, chars_to_divide_in_to):
#                     result_from_divide += input_data[first_arg + i]
#                     print(result_from_divide)
#         else:
#             if len(new_list[first_arg]) % second_arg == 0:
#                 chars_to_divide_in_to = len(new_list[first_arg]) / second_arg
#                 for i in range(0, chars_to_divide_in_to):
#                     result_from_divide += new_list[first_arg + i]
#                     print(result_from_divide)
#
#
#     command = input()
#
#
# print(new_list)
# print((" ".join(new_list)).strip())
#
# # abcd efgh ijkl mnop qrst uvwx yz
# # merge 4 10
# # divide 4 5
# # 3:1
