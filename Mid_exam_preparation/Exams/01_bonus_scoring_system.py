from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
attendances_for_max_student = 0


for _ in range(students):
    attendances = int(input())
    if lectures != 0:
        total_bonus = attendances / lectures * (5 + bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            attendances_for_max_student = attendances

print(f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {attendances_for_max_student} lectures.")

# not working with max_bonus = float("-inf")
# works without line 13 - bug in judge
