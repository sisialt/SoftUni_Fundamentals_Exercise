materials = {}
junks = {}
is_running = True

while is_running:
    input_data = input().split()

    for i in range(1, len(input_data), 2):
        material = input_data[i].lower()
        quantity = int(input_data[i - 1])

        if material == "shards" or material == "fragments" or material == "motes":
            if material not in materials:
                materials[material] = quantity
            else:
                materials[material] += quantity

            if materials[material] >= 250:
                if material == "shards":
                    print(f"Shadowmourne obtained!")
                elif material == "fragments":
                    print(f"Valanyr obtained!")
                elif material == "motes":
                    print(f"Dragonwrath obtained!")
                materials[material] -= 250
                is_running = False
                break

        else:
            if material not in junks:
                junks[material] = quantity
            else:
                junks[material] += quantity

print(f"shards: {materials.get('shards', 0)}")
print(f"fragments: {materials.get('fragments', 0)}")
print(f"motes: {materials.get('motes', 0)}")

for key, value in junks.items():
    print(f"{key}: {value}")


# materials = {
#     "shards": 0,
#     "fragments": 0,
#     "motes": 0
# }
# junks = {}
#
# legendary_item_by_material = {
#     "shards": "Shadowmourne",
#     "fragments": "Valanyr",
#     "motes": "Dragonwrath"
# }
#
# is_running = True
#
# while is_running:
#     input_data = input().split()
#
#     for i in range(1, len(input_data), 2):
#         material = input_data[i].lower()
#         quantity = int(input_data[i - 1])
#
#         if material in materials:
#             materials[material] += quantity
#
#             if materials[material] >= 250:
#                 materials[material] -= 250
#                 is_running = False
#                 print(f"{legendary_item_by_material[material]} obtained!")
#                 break
#
#         else:
#             if material not in junks:
#                 junks[material] = quantity
#             else:
#                 junks[material] += quantity
#
# for key, value in materials.items():
#     print(f"{key}: {value}")
#
# for key, value in junks.items():
#     print(f"{key}: {value}")
