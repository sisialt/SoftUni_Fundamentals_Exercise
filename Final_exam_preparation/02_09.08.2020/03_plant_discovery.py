n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = [int(rarity), []]

while True:
    line = input()
    if line == "Exhibition":
        break

    line_args = line.split(": ")
    command = line_args[0]

    if command == "Rate":
        command_args = line_args[1].split(" - ")
        current_plant = command_args[0]
        if current_plant not in plants:
            print("error")
            continue
        current_rating = int(command_args[1])

        plants[current_plant][1].append(current_rating)

    elif command == "Update":
        command_args = line_args[1].split(" - ")
        current_plant = command_args[0]
        if current_plant not in plants:
            print("error")
            continue
        new_rarity = int(command_args[1])

        plants[current_plant][0] = new_rarity

    elif command == "Reset":
        current_plant = line_args[1]
        if current_plant not in plants:
            print("error")
            continue

        plants[current_plant][1].clear()

print(f"Plants for the exhibition:")
for plant_name, value in plants.items():
    if value[1]:
        average_rating = sum(value[1])/len(value[1])
    else:
        average_rating = 0
    print(f"- {plant_name}; Rarity: {value[0]}; Rating: {average_rating:.2f}")
