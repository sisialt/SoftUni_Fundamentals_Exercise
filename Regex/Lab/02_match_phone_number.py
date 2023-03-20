import re

line = input()

pattern = r"\+359 2 \d{3} \d{4}|\+359\-2\-\d{3}\-\d{4}\b"

results = re.findall(pattern, line)
print(*results, sep=", ")

# findall with separator as group and the match is also a group

# pattern = r"(\+359( |\-)2\2\d{3}\2\d{4}\b)"
#
# phone_numbers = re.findall(pattern, line)
# i = 0
# for phone in phone_numbers:
#     if i != len(phone_numbers) - 1:
#         print(phone[0], end=", ")
#     else:
#         print(phone[0])
#     i += 1

# change group separator number in regex (\2, not \1, since there are 2 groups now)
# to not print the last result with ", " at the end, use counter i


# 2 - findall, 2 groups

# phone_numbers = re.findall(pattern, line)
# result = []
# for phone in phone_numbers:
#     for ph in phone:
#         if ph == " " or ph == "-":
#             continue
#         result.append(ph)
#
# print(*result, sep=", ")



# import re
#
# phone_numbers = []
# line = input()
#
# pattern = r"\+359( |\-)2\1\d{3}\1\d{4}\b"
#
# phone_numbers.extend(re.finditer(pattern, line))
# for phone in phone_numbers:
#     if phone != phone_numbers[len(phone_numbers) - 1]:
#         print(phone.group(), end=", ")
#     else:
#         print(phone.group())

# make empty list -> extend it with match objects, to print them use group()

