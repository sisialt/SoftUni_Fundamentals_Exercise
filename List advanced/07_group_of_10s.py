from math import ceil

numbers = [int(x) for x in input().split(", ")]

low_limit, high_limit = 1, 10
groups_count = ceil(max(numbers) / 10)

for i in range(1, groups_count + 1):
    grouped_numbers = [x for x in numbers if low_limit <= x <= high_limit]
    print(f"Group of {10 * i}'s: {grouped_numbers}")

    low_limit += 10
    high_limit += 10

# numbers_filtered = numbers.copy()
#
# bottom_limit, upper_limit = 0, 10
#
# while numbers_filtered:
#     group = []
#
#     for num in numbers:
#         if bottom_limit < num <= upper_limit:
#             group.append(num)
#             numbers_filtered.remove(num)
#
#     print(f"Group of {upper_limit}'s: {group}")
#
#     bottom_limit += 10
#     upper_limit += 10
#     numbers = numbers_filtered.copy()

