string = input()
new_string = string.strip()
list_from_string = string.split()
result = ""

while True:
    new_string = new_string.strip()
    new_string = new_string.strip("a")
    for el in list_from_string:
        if "a" in el:
            result += el.strip("a")
        else:
            result += el
    if "a" not in list_from_string:
        break
print(result)


#ahsa ajaj     hgj hakc nn
