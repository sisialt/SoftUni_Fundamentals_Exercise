while True:
    string = input()

    if string == "End":
        break
    elif string == "SoftUni":
        continue

    doubled_chars = ""

    for ch in string:
        doubled_chars += 2 * ch

    print(doubled_chars)