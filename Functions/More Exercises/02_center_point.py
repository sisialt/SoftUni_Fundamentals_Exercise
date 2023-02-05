import math


def close_to_coordinate_system(x, y):
    c = math.sqrt(x ** 2 + y ** 2)
    return c


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if close_to_coordinate_system(x1, y1) <= close_to_coordinate_system(x2, y2):
    print(f"({math.floor(x1)}, {math.floor(y1)})")
else:
    print(f"({math.floor(x2)}, {math.floor(y2)})")

