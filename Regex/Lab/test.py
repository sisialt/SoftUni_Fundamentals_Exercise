import re

line = input()

pattern = r"(\+359( |\-)2\2\d{3}\2\d{4}\b)"

phone_numbers = re.findall(pattern, line)
result = []
for phone in phone_numbers:
    for ph in phone:
        if ph == " " or ph == "-":
            continue
        result.append(ph)

print(*result, sep=", ")
# # use re.finditer(), make empty list -> extend it with match objects, to print them use group()

# text = input()
#
# pattern = r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z0-9\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"
#
# result = re.findall(pattern, text)
#
# print("\n".join([res[0] for res in result]))