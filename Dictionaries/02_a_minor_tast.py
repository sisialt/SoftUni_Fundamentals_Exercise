sequence = input()

resources = []
resources_dict = {}

while sequence != "stop":
    resources.append(sequence)
    sequence = input()

for index, el in enumerate(resources):
    if index % 2 == 0:
        if el not in resources_dict:
            resources_dict[el] = int(resources[index + 1])
        else:
            resources_dict[el] += int(resources[index + 1])

for key, value in resources_dict.items():
    print(f"{key} -> {value}")


# sequence = input()
#
# resources_dict = {}
#
# while sequence != "stop":
#     quantity = int(input())
#
#     if sequence not in resources_dict:
#         resources_dict[sequence] = quantity
#     else:
#         resources_dict[sequence] += quantity
#
#     sequence = input()
#
# for key, value in resources_dict.items():
#     print(f"{key} -> {value}")
