route = input().split("||")
fuel = int(input())
ammunition = int(input())

# Travel 10||Enemy 30||Repair 15||Titan
# 50
# 80

# Travel 20||Enemy 50||Enemy 50||Enemy 10||Repair 15||Enemy 50||Titan
# 60
# 100

for element in route:
    command = element.split()[0]

    if command == "Travel":
        light_years = int(element.split()[1])
        if fuel >= light_years:
            fuel -= light_years
            print(f"The spaceship travelled {light_years} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        enemys_armour = int(element.split()[1])
        if ammunition >= enemys_armour:
            ammunition -= enemys_armour
            print(f"An enemy with {enemys_armour} armour is defeated.")
        else:
            if fuel >= 2 * enemys_armour:
                fuel -= 2 * enemys_armour
                print(f"An enemy with {enemys_armour} armour is outmaneuvered.")
            else:
                print(f"Mission failed.")
                break

    elif command == "Repair":
        ammunition_and_fuel_added = int(element.split()[1])
        fuel += ammunition_and_fuel_added
        ammunition += 2 * ammunition_and_fuel_added
        print(f"Ammunitions added: {2 * ammunition_and_fuel_added}.")
        print(f"Fuel added: {ammunition_and_fuel_added}.")

    elif command == "Titan":
        print(f"You have reached Titan, all passengers are safe.")

