guests_meals = {}
count_unliked_meals = 0

while True:
    line = input()
    if line == "Stop":
        break

    like, guest, meal = line.split("-")

    if like == "Like":
        if guest not in guests_meals:
            guests_meals[guest] = []

        if meal not in guests_meals[guest]:
            guests_meals[guest].append(meal)

    elif like == "Unlike":
        if guest not in guests_meals:
            print(f"{guest} is not at the party.")
            continue

        if meal not in guests_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            continue

        guests_meals[guest].remove(meal)
        count_unliked_meals += 1
        print(f"{guest} doesn't like the {meal}.")

sorted_guests_meals_by_len = dict(sorted(guests_meals.items(), key=lambda x: (-len(x[1]), x)))

for guest, meals in sorted_guests_meals_by_len.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {count_unliked_meals}")
