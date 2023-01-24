import math

people = int(input())
capacity_elevator = int(input())

courses_elevator = people / capacity_elevator

print(math.ceil(courses_elevator))