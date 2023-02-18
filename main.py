neighborhood = input().split("@")

integers_hood = [int(num) for num in neighborhood]
comand = input()

counter = 0
successful = 0
not_successful = 0

while comand != "Love!":

    acction, indx = comand.split()
    indx = int(indx)
    counter += indx

    if counter >= len(integers_hood):
        counter = 0

    if integers_hood[counter] == 0:
        print(f"Place {counter} already had Valentine's day.")
    else:
        integers_hood[counter] -= 2
        if integers_hood[counter] == 0:
            print(f"Place {counter} has Valentine's day.")

    comand = input()

print(f"Cupid's last position was {counter}.")

for integer_hood in integers_hood:
    if integer_hood == 0:
        successful += 1
    else:
        not_successful += 1

if not not_successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {not_successful} places.")
