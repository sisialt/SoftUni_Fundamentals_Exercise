password = input()

while True:
    line = input()
    if line == "Done":
        break

    line_args = line.split(" ")
    command = line_args[0]

    if command == "TakeOdd":
        odd_chars = ""
        for i in range(len(password)):
            if i % 2 == 1:
                odd_chars += password[i]

        password = odd_chars

    elif command == "Cut":
        index = int(line_args[1])
        length = int(line_args[2])

        substring = password[index:index + length]
        password = password.replace(substring, "", 1)

    elif command == "Substitute":
        substring = line_args[1]
        substitute = line_args[2]

        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue

    print(password)

print(f"Your password is: {password}")
