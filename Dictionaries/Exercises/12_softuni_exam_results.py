points_by_students = {}
students_by_languages = {}

while True:
    line = input()
    if line == "exam finished":
        break

    line_args = line.split("-")
    username = line_args[0]

    if len(line_args) != 2:
        language, points = line_args[1], int(line_args[2])

        if language not in students_by_languages:
            students_by_languages[language] = []

        if username not in points_by_students:
            points_by_students[username] = points
        else:
            for el in students_by_languages[language]:

                if el == username:
                    points_by_students[username] = max(points, points_by_students[username])
                    break
                else:
                    points_by_students[username] += points

        students_by_languages[language].append(username)

    else:
        points_by_students.pop(username)

print("Results:")
for name, points in points_by_students.items():
    print(f"{name} | {points}")

print("Submissions:")
for language, count in students_by_languages.items():
    print(f"{language} - {len(count)}")

# peter java  23, koko java 30, peter c 50, peter java 60
# peter 23 koko 30, java [peter, koko], peter [java, c]
