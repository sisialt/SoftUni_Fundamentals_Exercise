treasure = ["one", "two", "three", "four", "five", "six"]
stolen_items = []
count = min(0, len(treasure))
# stolen_items = treasure[-count:]
# treasure = treasure[:-count]
# print(", ".join(stolen_items))
# print(treasure)

# for i in range(count, 0, -1):
#     stolen_items.append(treasure.pop(-i))
#
# print(", ".join(stolen_items))
# print(treasure)
#
for i in range(-count, 0, 1):
    stolen_items.append(treasure[i])
    treasure.pop(i)
print(", ".join(stolen_items))
print(treasure)
