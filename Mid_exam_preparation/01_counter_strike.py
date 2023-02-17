initial_energy = int(input())
command = input()

energy = initial_energy
count_won_battles = 0

while command != "End of battle":
    distance = int(command)

    if distance <= energy:
        energy -= distance
        count_won_battles += 1
        if count_won_battles % 3 == 0:
            energy += count_won_battles
    else:
        print(f"Not enough energy! Game ends with {count_won_battles} won battles and {energy} energy")
        break

    command = input()

else:
    print(f"Won battles: {count_won_battles}. Energy left: {energy}")