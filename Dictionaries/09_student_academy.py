n = int(input())

academy = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in academy:
        academy[student_name] = [student_grade]
    else:
        academy[student_name].append(student_grade)

for student in academy:
    average_grade = sum(academy[student]) / len(academy[student])
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
