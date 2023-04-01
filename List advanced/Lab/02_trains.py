wagons = int(input())

train = [0] * wagons

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split()
    command = line_args[0]

    if command == "add":
        people = int(line_args[1])
        train[-1] += people

    elif command == "insert":
        index = int(line_args[1])
        people = int(line_args[2])
        train[index] += people

    elif command == "leave":
        index = int(line_args[1])
        people = int(line_args[2])
        train[index] -= people

print(train)
