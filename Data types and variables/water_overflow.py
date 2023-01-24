n = int(input())

total_liters = 0

for _ in range(n):
    liters_of_water_to_pour = int(input())

    if liters_of_water_to_pour > 255 - total_liters:
        print("Insufficient capacity!")
        continue

    total_liters += liters_of_water_to_pour

print(total_liters)
