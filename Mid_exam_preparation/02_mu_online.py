initial_health = 100
initial_bitcoins = 0

rooms = input().split("|")

health = 100
bitcoins = 0
is_dead = False

for room in rooms:
    room_args = room.split()
    command = room_args[0]
    number = int(room_args[1])

    # rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000

    if command == "potion":
        if health + number <= 100:
            health = health + number
            amount = number
        else:
            amount = initial_health - health
            health = initial_health

        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")