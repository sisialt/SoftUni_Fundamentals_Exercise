fire_input = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0
cells_done = []
# print("Cells:")

for fire in fire_input:
    fire_list = fire.split()
    value = fire_list[-1]
    value = int(value)
    fire_level = fire_list[0]

    if fire_level == "High":
        if value < 81 or value > 125:
            continue
    elif fire_level == "Medium":
        if value < 51 or value > 80:
            continue
    elif fire_level == "Low":
        if value < 1 or value > 50:
            continue

    if water_amount < value:
        continue

    water_amount -= value
    effort += 0.25 * value
    total_fire += value
    cells_done.append(value)
    # print(f" - {value}")

print("Cells:")
for cell in cells_done:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250
