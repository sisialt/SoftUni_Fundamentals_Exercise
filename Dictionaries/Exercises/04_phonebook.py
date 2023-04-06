input_data = input()

phonebook = {}

while input_data[0].isalpha():
    name, phone = input_data.split("-")
    phonebook[name] = phone

    input_data = input()

for _ in range(int(input_data)):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
