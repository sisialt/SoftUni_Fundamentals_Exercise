message = input()

while True:
    line = input()
    if line == "Reveal":
        break

    line_args = line.split(":|:")
    command = line_args[0]

    if command == "InsertSpace":
        index = int(line_args[1])
        message = message[:index] + " " + message[index:]

    elif command == "Reverse":
        substring = line_args[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            message = message + reversed_substring
        else:
            print("error")
            continue

    elif command == "ChangeAll":
        substring = line_args[1]
        replacement = line_args[2]

        message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")

# heVVodar!gniV
# ChangeAll:|:V:|:l
# Reverse:|:!gnil
# InsertSpace:|:5
# Reveal


