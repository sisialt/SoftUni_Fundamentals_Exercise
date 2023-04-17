def calculate_sum_digits(number_as_string):
    sum_even, sum_odd = 0, 0
    for num in number_as_string:
        if int(num) % 2 == 0:
            sum_even += int(num)
        else:
            sum_odd += int(num)

    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()

print(calculate_sum_digits(number))


# def calculate_sum_digits(number_as_string):
#     sum_even, sum_odd = 0, 0
#     for num in number_as_string:
#         if int(num) % 2 == 0:
#             sum_even += int(num)
#         else:
#             sum_odd += int(num)
#
#     return [sum_even, sum_odd]
#
#
# number = input()
# result = calculate_sum_digits(number)
# print(f"Odd sum = {result[1]}, Even sum = {result[0]}")


