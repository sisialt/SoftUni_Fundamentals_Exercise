cities = {}

while True:
    line = input()
    if line == "Sail":
        break

    line_args = line.split("||")
    city = line_args[0]
    population = int(line_args[1])
    gold = int(line_args[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split("=>")
    town = line_args[1]

    if line_args[0] == "Plunder":
        people = int(line_args[2])
        gold_stolen = int(line_args[3])

        cities[town]["population"] -= people
        cities[town]["gold"] -= gold_stolen

        print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")

        if cities[town]["population"] <= 0 or cities[town]["gold"] <= 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif line_args[0] == "Prosper":
        gold_added = int(line_args[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
            continue

        cities[town]["gold"] += gold_added

        print(f"{gold_added} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key_town, value_people_gold in cities.items():
        print(f"{key_town} -> Population: {value_people_gold['population']} citizens, Gold: {value_people_gold['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

#     if city not in cities:
#         cities[city] = [population, gold]  # cities[city] = {"population": population, "gold": gold}
#     else:
#         cities[city][0] += population  # cities[city]["population"] += population
#         cities[city][1] += gold  # -> ["gold"]
#
# while True:
#     line = input()
#     if line == "End":
#         break
#
#     line_args = line.split("=>")
#     town = line_args[1]
#
#     if line_args[0] == "Plunder":
#         people = int(line_args[2])
#         gold_stolen = int(line_args[3])
#
#         cities[town][0] -= people  # cities[town]["population"] -= people
#         cities[town][1] -= gold_stolen  # -> ["gold"]
#
#         print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
#
#         if cities[town][0] <= 0 or cities[town][1] <= 0:
#             cities.pop(town)
#             print(f"{town} has been wiped off the map!")
#
#     elif line_args[0] == "Prosper":
#         gold_added = int(line_args[2])
#         if gold_added < 0:
#             print("Gold added cannot be a negative number!")
#             continue
#
#         cities[town][1] += gold_added
#
#         print(f"{gold_added} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
#
# if cities:
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for key_town, value_people_gold in cities.items():
#         print(f"{key_town} -> Population: {value_people_gold[0]} citizens, Gold: {value_people_gold[1]} kg")
#
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")
