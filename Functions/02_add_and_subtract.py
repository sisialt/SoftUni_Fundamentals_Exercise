def sum_numbers(n1, n2):
    sum_num = n1 + n2
    return sum_num


def subtract(sum1_2, n3):
    subtract_sum_n3 = sum1_2 - n3
    return subtract_sum_n3


# def add_and_subtract(n1, n2, n3):
#     sum_numbers(n1, n2)
#     add_and_subt = subtract(sum_numbers(n1, n2), n3)
#     return add_and_subt


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = sum_numbers(num1, num2)
end_result = subtract(result, num3)

print(end_result)
