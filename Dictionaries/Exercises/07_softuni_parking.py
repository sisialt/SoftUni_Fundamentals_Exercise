n = int(input())

parking = {}

for _ in range(n):
    command = input().split()

    action = command[0]
    username = command[1]

    if action == "register":

        license_plate_number = command[2]

        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":

        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking.pop(username)

for key, value in parking.items():
    print(f"{key} => {value}")
