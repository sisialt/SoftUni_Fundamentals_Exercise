people = int(input())
wagons = [int(x) for x in input().split(" ")]

MAX_PEOPLE_IN_WAGON = 4
people_in_wagon = 0
total_people_in_lift = 0

for index, wagon in enumerate(wagons):

    people_in_wagon = int(wagon)
    free_places_in_wagon = MAX_PEOPLE_IN_WAGON - people_in_wagon
    if free_places_in_wagon == 0:
        continue

    if people + people_in_wagon > MAX_PEOPLE_IN_WAGON:
        people -= free_places_in_wagon
        people_in_wagon += free_places_in_wagon
    else:
        people_in_wagon = people + people_in_wagon
        people -= people_in_wagon

    people = max(0, people)
    total_people_in_lift += people_in_wagon

    wagons.pop(index)
    wagons.insert(index, people_in_wagon)

if people:
    print(f"There isn't enough space! {people} people in a queue!\n{' '. join(str(x) for x in wagons)}")
else:
    if total_people_in_lift == MAX_PEOPLE_IN_WAGON * len(wagons):
        print(*wagons, sep=" ")
    else:
        print(f"The lift has empty spots!\n{' '.join(str(x) for x in wagons)}")

# forgot to validate no -people: line 22
# forgot line 12
