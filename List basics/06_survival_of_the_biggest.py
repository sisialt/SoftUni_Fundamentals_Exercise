# numbers = input().split()
# numbers_as_integers_list = []
# for number in numbers:
#     number = int(number)
#     numbers_as_integers_list.append(number)

numbers_as_integers_list = [int(x) for x in input().split()]

n = int(input())
# sorted_numbers = sorted(numbers_as_integers_list)
# for i in range(n):
#     numbers_as_integers_list.remove(sorted_numbers[i])

for _ in range(n):
    min_num = min(numbers_as_integers_list)
    numbers_as_integers_list.remove(min_num)

print(", ".join([str(x) for x in numbers_as_integers_list]))

# for i in range(len(numbers_as_integers_list)):
#     num = numbers_as_integers_list[i]
#     if i == len(numbers_as_integers_list) - 1:
#         print(num)
#     else:
#         print(num, end=", ")

