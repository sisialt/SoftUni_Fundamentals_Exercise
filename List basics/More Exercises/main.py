#
#
def sum_nums():
    print(5 + 5)

print(sum_nums())






# # 1 8 8 7 6 4 2 1
# #
# # 1 2 4 6 7 8 8 1
# #
# # 2 6 9 4 9 5 8 9
# #
# # 9 8 5 9 4 9 6 2
#
# numbers = [int(x) for x in input().split()]
#
# # print(sorted(numbers))
# print(numbers)
# print(f"index not reversed {numbers.index(max(numbers))}")
# numbers.reverse()
# print(f"reversed{numbers}")
# print(f"index max reversed{numbers.index(max(numbers))}")
# print(f"index max right in original with more max {len(numbers) - numbers.index(max(numbers)) - 1}")
#
# # #sled len i = k * i - len
# #
# # numbers_without_executed = numbers.copy()
# # executed_list = []
# # counter = 0
# #
# # for i in range(1, len(numbers) + 1):
# #     number_for_execution = k * i
# #     if number_for_execution > len(numbers):
# #         number_for_execution -= len(numbers)
# #         if counter < 3:
# #             executed_list.append(numbers[number_for_execution - 1])
# #             numbers_without_executed.pop(number_for_execution - 1)
# #         else:
# #             executed_list.append(numbers_without_executed[number_for_execution - 1])
# #             numbers_without_executed.pop(number_for_execution - 1)
# #     else:
# #         executed_list.append(numbers[number_for_execution - 1])
# #         numbers_without_executed.pop(number_for_execution - i)
# #
# # print(numbers)
# # print(number_for_execution)
# # print(numbers_without_executed)
# # print(executed_list)
# #
