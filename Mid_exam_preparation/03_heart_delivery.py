neighborhood = [int(x) for x in input().split("@")]

current_position = 0
count_houses_without_valentines_day = 0

while True:
    command = input()
    if command == "Love!":
        break

    length = int(command.split()[1])
    current_position += length

    if current_position >= len(neighborhood):
        current_position = 0

    if neighborhood[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        neighborhood[current_position] -= 2
        if neighborhood[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")

print(f"Cupid's last position was {current_position}.")

# for house in neighborhood:
#     if house == 0:
#         count_houses_with_valentines_day += 1
#     else:
#         count_houses_without_valentines_day += 1

count_houses_without_valentines_day = [1 for x in neighborhood if x != 0]
if sum(count_houses_without_valentines_day) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {sum(count_houses_without_valentines_day)} places.")

# if count_houses_with_valentines_day == len(neighborhood):
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {count_houses_without_valentines_day} places.")

