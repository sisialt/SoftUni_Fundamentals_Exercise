def check_grades(gr):
    if 2.00 <= gr < 3.00:
        print("Fail")
    elif 3.00 <= gr < 3.50:
        print("Poor")
    elif 3.50 <= gr < 4.50:
        print("Good")
    elif 4.50 <= gr < 5.50:
        print("Very Good")
    elif 5.50 <= gr < 6.00:
        print("Excellent")


grade = float(input())
check_grades(grade)
