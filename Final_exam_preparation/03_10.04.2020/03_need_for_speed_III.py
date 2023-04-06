n = int(input())

cars = {}

for _ in range(n):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])

    cars[car] = [mileage, fuel]

while True:
    line = input()
    if line == "Stop":
        break

    line_args = line.split(" : ")
    command = line_args[0]
    car = line_args[1]

    if command == "Drive":
        distance = int(line_args[2])
        fuel_for_distance = int(line_args[3])

        if fuel_for_distance > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel_for_distance

            print(f"{car} driven for {distance} kilometers. {fuel_for_distance} liters of fuel consumed.")

            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel_to_add = int(line_args[2])

        if cars[car][1] + fuel_to_add > 75:
            fuel_to_add = 75 - cars[car][1]
        cars[car][1] += fuel_to_add
        print(f"{car} refueled with {fuel_to_add} liters")

    elif command == "Revert":
        reverted_kilometers = int(line_args[2])

        cars[car][0] -= reverted_kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {reverted_kilometers} kilometers")

for car in cars:
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")
