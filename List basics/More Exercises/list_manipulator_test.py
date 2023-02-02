numbers = [int(x) for x in input().split()]

even_numbers, odd_numbers = [], []

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])

while True:
    command = input()
    if command == "end":
        break

    command = command.split()

    if command[0] == "exchange":
        if int(command[1]) > len(numbers) or int(command[1]) < 0:
            print("Invalid index")
        else:
            for i in range(int(command[1]) + 1):
                numbers.append(numbers[i])
            for i in range(int(command[1]) + 1):
                numbers.pop(0)

    elif command[0] == "max":
        if command[1] == "even":
            if len(even_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(max(even_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")
        elif command[1] == "odd":
            if len(odd_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(max(odd_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            if len(even_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(min(even_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")
        elif command[1] == "odd":
            if len(odd_numbers) > 0:
                numbers.reverse()
                print(len(numbers) - numbers.index(min(odd_numbers)) - 1)
                numbers.reverse()
            else:
                print("No matches")

    elif command[0] == "first":

        if int(command[1]) > len(numbers):
            print("Invalid count")
            continue

        first_list, even_numbers, odd_numbers = [], [], []

        for i in range(0, len(numbers)):
            if numbers[i] % 2 == 0:
                even_numbers.append(numbers[i])
            else:
                odd_numbers.append(numbers[i])

        if command[2] == "even":
            if int(command[1]) <= len(even_numbers):
                for i in range(0, int(command[1])):
                    first_list.insert(i, even_numbers[i])
                print(first_list)
            else:
                print(even_numbers)
        elif command[2] == "odd":
            if int(command[1]) <= len(odd_numbers):
                for i in range(0, int(command[1])):
                    first_list.insert(i, odd_numbers[i])
                print(first_list)
            else:
                print(odd_numbers)

    elif command[0] == "last":

        if int(command[1]) > len(numbers):
            print("Invalid count")
            continue

        last_list, even_numbers, odd_numbers = [], [], []

        for i in range(0, len(numbers)):
            if numbers[i] % 2 == 0:
                even_numbers.append(numbers[i])
            else:
                odd_numbers.append(numbers[i])

        if command[2] == "even":
            if int(command[1]) <= len(even_numbers):
                for i in range(0, int(command[1])):
                    last_list.insert(i, even_numbers[i])
                print(last_list)
            else:
                print(even_numbers)

        elif command[2] == "odd":
            if int(command[1]) <= len(odd_numbers):
                for i in range(0, int(command[1])):
                    last_list.insert(i, odd_numbers[i])
                print(last_list)
            else:
                print(odd_numbers)

print(numbers)
