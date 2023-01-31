n = int(input())

brackets_list = []
balanced = True

for _ in range(n):
    string = input()
    if string == "(":
        brackets_list.append(string)
    elif string == ")":
        brackets_list.append(string)

for i in range(0, len(brackets_list)):
    if (i % 2 == 0 and brackets_list[i] != "(") or (i % 2 != 0 and brackets_list[i] != ")"):
        balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


# n = int(input())
#
# brackets = 0
#
# for bracket in range(1, n + 1):
#     string = input()
#
#     if string == "(":
#         brackets += 1
#     elif string == ")":
#         brackets -= 1
#
#     if brackets != 0 and brackets != 1:
#         print("UNBALANCED")
#         break
#
# else:
#     print("BALANCED")