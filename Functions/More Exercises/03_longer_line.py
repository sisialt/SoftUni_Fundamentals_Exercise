import math


def find_longer_line(x, y):
    c = math.sqrt(x ** 2 + y ** 2)
    return c


def print_closer_point(x1, y1, x2, y2):
    if find_longer_line(x1, y1) <= find_longer_line(x2, y2):
        return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line_first_points = find_longer_line((abs(x1 - x2)), abs(y1 - y2))
line_second_point = find_longer_line((abs(x3 - x4)), abs(y3 - y4))

if line_first_points >= line_second_point:
    print(print_closer_point(x1, y1, x2, y2))

else:
    print(print_closer_point(x3, y3, x4, y4))