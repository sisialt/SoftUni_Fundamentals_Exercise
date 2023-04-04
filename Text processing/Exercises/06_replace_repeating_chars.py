string = input()
# string_without_repeating_chars = ""
#
# # for i, ch in enumerate(string):
#     if i != len(string) - 1 and ch == string[i + 1]:
#         string_without_repeating_chars += ""    # continue
#         i += 1
#     else:
#         string_without_repeating_chars += ch
#
# print(string_without_repeating_chars)

string_without_repeating_chars = string[0]

for ch in string:
    if ch == string_without_repeating_chars[-1]:
        continue
    string_without_repeating_chars += ch

print(string_without_repeating_chars)
