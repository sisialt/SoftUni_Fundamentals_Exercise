gifts = input().split()

while True:

    command = input()
    if command == "No Money":
        break

    command_list = command.split()

    if command_list[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command_list[1]:
                gifts[i] = "None"
        # for gift in gifts:
        #     if command_list[1] == gift:
        #         idx = gifts.index(gift)
        #         gifts.pop(idx)
        #         gifts.insert(idx, "None")

    elif command_list[0] == "Required":
        if 0 < int(command_list[2]) < len(gifts):
            gifts[int(command_list[2])] = command_list[1]
            # gifts.pop(int(command_list[2]))
            # gifts.insert(int(command_list[2]), command_list[1])

    elif command_list[0] == "JustInCase":
        gifts[-1] = command_list[1]

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=" ")

# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Egg
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
