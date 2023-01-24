is_voldemort = False

while True:
    name = input()

    if name == "Welcome!":
        break
    elif name == "Voldemort":
        is_voldemort = True
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if not is_voldemort:
    print("Welcome to Hogwarts.")