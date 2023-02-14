pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health_capacity = int(input())

repair_count = 0
is_winner = False
is_running = True

while is_running:
    command = input()
    if command == "Retire":
        break

    command_as_list = command.split()
    action = command_as_list[0]

    if action == "Fire":
        index = int(command_as_list[1])
        damage = int(command_as_list[2])

        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_winner = True
                break

    elif action == "Defend":
        start_idx = int(command_as_list[1])
        end_idx = int(command_as_list[2])
        damage = int(command_as_list[3])

        if 0 <= start_idx < len(pirate_ship) and 0 <= end_idx < len(pirate_ship):

            for i in range(start_idx, end_idx + 1):
                pirate_ship[i] -= damage

                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_winner = True
                    is_running = False
                    break

    elif action == "Repair":
        index = int(command_as_list[1])
        health = int(command_as_list[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity

    elif action == "Status":

        for section in pirate_ship:
            if section < max_health_capacity * 0.2:
                repair_count += 1

        print(f"{repair_count} sections need repair.")

if not is_winner:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
# 12>13>11>20>66
# 12>22>33>44>55>32>18
# 70
# Fire 2 40
# Retire
