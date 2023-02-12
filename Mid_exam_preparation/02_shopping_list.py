shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    command_as_list = command.split()
    action = command_as_list[0]
    item = command_as_list[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif action == "Correct":
        new_item = command_as_list[2]
        if item in shopping_list:
            shopping_list.insert(shopping_list.index(item), new_item)
            shopping_list.remove(item)

    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.append(item)
            shopping_list.remove(item)

print(", ".join(shopping_list))
