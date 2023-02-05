def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


numbers = [int(x) for x in input().split()]

even_numbers = list(filter(even_or_odd, numbers))

print(even_numbers)


# even_nums = []
#
# even_numbers = filter(even_or_odd, numbers)
#
# for number in even_numbers:
#     even_nums.append(number)
#
# print(even_nums)
