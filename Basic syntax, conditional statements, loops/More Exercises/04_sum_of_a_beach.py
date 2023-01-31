words = input().lower()

total_count = words.count('sand') + words.count('water') + words.count('fish') + words.count('sun')

print(total_count)

# when you dont want it that easy...
#
# string = input()
# list_of_string = list(string)
#
# count = 0
#
# for i in range(0, len(string)):
#
#     if list_of_string[i] == "w" or list_of_string[i] == "W":
#         if 4 < len(string) - i:
#             if list_of_string[i + 1] == "a" or list_of_string[i + 1] == "A":
#                 if list_of_string[i + 2] == "t" or list_of_string[i + 2] == "T":
#                     if list_of_string[i + 3] == "e" or list_of_string[i + 3] == "E":
#                         if list_of_string[i + 4] == "r" or list_of_string[i + 4] == "R":
#                             i += 5
#                             count += 1
#
#     elif list_of_string[i] == "s" or list_of_string[i] == "S":
#         if 3 < len(string) - i:
#             if list_of_string[i + 1] == "a" or list_of_string[i + 1] == "A":
#                 if list_of_string[i + 2] == "n" or list_of_string[i + 2] == "N":
#                     if list_of_string[i + 3] == "d" or list_of_string[i + 3] == "D":
#                         i += 4
#                         count += 1
#             elif list_of_string[i + 1] == "u" or list_of_string[i + 1] == "U":
#                 if list_of_string[i + 2] == "n" or list_of_string[i + 2] == "N":
#                     i += 3
#                     count += 1
#
#     elif list_of_string[i] == "f" or list_of_string[i] == "F":
#         if 3 < len(string) - i:
#             if list_of_string[i + 1] == "i" or list_of_string[i + 1] == "I":
#                 if list_of_string[i + 2] == "s" or list_of_string[i + 2] == "S":
#                     if list_of_string[i + 3] == "h" or list_of_string[i + 3] == "H":
#                         i += 4
#                         count += 1
#
# print(count)
