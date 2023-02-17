food = float(input())
hay = float(input())
cover = float(input())
guineas_weight = float(input())

food_left = food
hay_left = hay
cover_left = cover

for day in range(1, 31):
    food_left -= 0.30
    if day % 2 == 0:
        hay_left -= 0.05 * food_left

    if day % 3 == 0:
        cover_left -= guineas_weight / 3

    if food_left <= 0 or hay_left <= 0 or cover_left <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_left:.2f}, Hay: {hay_left:.2f}, Cover: {cover_left:.2f}.")

# convert to grams, else not right float, if 0.3 -> 0.30
# line 18 must be at the end of the for-loop, not at the beginning
