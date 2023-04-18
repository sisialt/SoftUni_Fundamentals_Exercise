first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

total_students_for_one_hour = first_employee + second_employee + third_employee

hours_needed = 0
break_hours = 0

while students_count > 0:
    hours_needed += 1
    students_count -= total_students_for_one_hour
    if hours_needed % 4 == 0:
        break_hours += 1

print(f"Time needed: {hours_needed + break_hours}h.")

# first_employee = int(input())
# second_employee = int(input())
# third_employee = int(input())
# students_count = int(input())
#
# total_students_for_one_hour = first_employee + second_employee + third_employee
#
# hours_needed = 0
#
# while students_count > 0:
#     hours_needed += 1
#     if hours_needed % 4 == 0:
#         continue
#     students_count -= total_students_for_one_hour
#
# print(f"Time needed: {hours_needed}h.")

