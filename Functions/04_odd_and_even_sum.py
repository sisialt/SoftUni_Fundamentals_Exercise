def calculate_sum_digits(number_as_string, sum_evens, sum_odds):

    for num in number_as_string:
        if int(num) % 2 == 0:
            sum_evens += int(num)
        else:
            sum_odds += int(num)

    return f"Odd sum = {sum_odds}, Even sum = {sum_evens}"


number = input()

sum_even, sum_odd = 0, 0

print(calculate_sum_digits(number, sum_even, sum_odd))





