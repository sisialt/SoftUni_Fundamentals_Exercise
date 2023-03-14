# string_input = input()
# new_string = ""
# result = ""
#
# while len(string_input):
#     for i in range(len(string_input)):
#         if string_input[i] == ">":
#             result = string_input[:i + 1]
#             break
#     else:
#         result = string_input
#
#     string_input = string_input.replace(result, "")
#     new_string += result
#
#     if string_input:
#         if string_input[0].isdigit():
#             explosion = int(string_input[0])
#             for n in range(explosion):
#                 string_input = string_input.replace(string_input[0], "", 1)
#         else:
#             new_string += string_input
#             string_input = ""
#
# print(new_string)
# print(string_input)
#
#
text = "ab12"
for i in range(len(text)):
    if int(text[i]):
        print("hi")