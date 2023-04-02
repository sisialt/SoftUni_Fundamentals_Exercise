employees_happiness = [int(x) for x in input().split()]
factor = int(input())

employees_happiness_multiplied = [el * factor for el in employees_happiness]
average = sum(employees_happiness_multiplied) / len(employees_happiness_multiplied)

count_happy = len([el for el in employees_happiness_multiplied if el >= average])
count_unhappy = len(employees_happiness_multiplied) - count_happy

if count_happy >= count_unhappy:
    print(f"Score: {count_happy}/{len(employees_happiness_multiplied)}. Employees are happy!")
else:
    print(f"Score: {count_happy}/{len(employees_happiness_multiplied)}. Employees are not happy!")
