numbers = [int(x) for x in input().split(", ")]

zeros = 0
new_numbers = numbers.copy()

for i in range(0, len(numbers)):
    if numbers[i] == 0:
        new_numbers.remove(numbers[i])
        zeros += 1

for _ in range(zeros):
    new_numbers.append(0)

print(new_numbers)


# numbers = input().split(", ")
#
# zeros = 0
# new_numbers = numbers.copy()
#
# for i in range(0, len(numbers)):
#     if numbers[i] == "0":
#         new_numbers.remove(numbers[i])
#         zeros += 1
#
# for _ in range(zeros):
#     new_numbers.append("0")
#
# print(new_numbers)
