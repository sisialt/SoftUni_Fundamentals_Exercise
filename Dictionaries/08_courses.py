input_data = input()

courses = {}

while input_data != "end":
    course, student = input_data.split(" : ")

    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)

    input_data = input()

for key in courses:
    print(f"{key}: {len(courses[key])}")
    for i in range(len(courses[key])):
        print(f"-- {courses[key][i]}")
