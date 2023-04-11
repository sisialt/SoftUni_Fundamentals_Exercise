line = input()

courses = {}

while ":" in line:
    name, name_id, course = line.split(":")

    if course not in courses:
        courses[course] = {}
    courses[course][name] = name_id

    line = input()

line = line.replace("_", " ")

for name, name_id in courses[line].items():
    print(f"{name} - {name_id}")