events = input().split("|")

initial_energy = 100
initial_coins = 100
current_energy = initial_energy
current_coins = initial_coins
closed = False

for event in events:
    event_args = event.split("-")
    event_ingredient = event_args[0]
    value = int(event_args[1])
    # earned_coins = 0
    # gained_energy = 0

    if event_ingredient == "rest":
        if current_energy + value <= initial_energy:
            current_energy += value
            # gained_energy = value
            print(f"You gained {value} energy.")
        else:
            print(f"You gained {initial_energy - current_energy} energy.")
            current_energy = initial_energy

        print(f"Current energy: {current_energy}.")

    elif event_ingredient == "order":
        if current_energy >= 30:
            # earned_coins += value
            current_coins += value
            current_energy -= 30
            print(f"You earned {value} coins.")

        else:
            current_energy += 50
            print(f"You had to rest!")

    else:
        if value <= current_coins:
            current_coins -= value
            print(f"You bought {event_ingredient}.")
        else:
            closed = True
            print(f"Closed! Cannot afford {event_ingredient}.")
            break

if not closed:
    print(f"Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}")