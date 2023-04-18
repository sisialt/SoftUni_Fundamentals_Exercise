def check_password(password):
    result = ""
    count_digits = 0
    is_valid = True

    if not 6 <= len(password) <= 10:
        result += "Password must be between 6 and 10 characters\n"
        is_valid = False

    for ch in password:
        if 48 <= ord(ch) <= 57:
            count_digits += 1

        if not (48 <= ord(ch) <= 57 or 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122):
            result += "Password must consist only of letters and digits\n"
            is_valid = False
            break

    if not count_digits >= 2:
        result += "Password must have at least 2 digits"
        is_valid = False

    if is_valid:
        return "Password is valid"
    else:
        return result


password_input = input()

print(check_password(password_input))
