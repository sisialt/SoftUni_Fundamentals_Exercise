pirates = {}

while True:
    line = input()
    if line == "Sail":
        break

    line_args = line.split("||")
    city = line_args[0]
    population = int(line_args[1])
    gold = int(line_args[2])

    if city not in pirates:
        pirates[city] = [population, gold]
    else:
        pirates[city][0] += population
        pirates[city][1] += gold

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split("=>")
    town = line_args[1]

    if line_args[0] == "Plunder":
        people = int(line_args[2])
        gold_stolen = int(line_args[3])

        pirates[town][0] -= people
        pirates[town][1] -= gold_stolen

        print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")

        if pirates[town][0] <= 0 or pirates[town][1] <= 0:
            pirates.pop(town)
            print(f"{town} has been wiped off the map!")

    elif line_args[0] == "Prosper":
        gold_added = int(line_args[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
            continue

        pirates[town][1] += gold_added

        print(f"{gold_added} gold added to the city treasury. {town} now has {pirates[town][1]} gold.")

if pirates:
    print(f"Ahoy, Captain! There are {len(pirates)} wealthy settlements to go to:")
    for key_town, value_people_gold in pirates.items():
        print(f"{key_town} -> Population: {value_people_gold[0]} citizens, Gold: {value_people_gold[1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
