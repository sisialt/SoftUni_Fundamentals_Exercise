text = input()

digits = []
chars = ""
result = ""

for ch in text:
    if ch.isdigit():
        digits.append(int(ch))
    else:
        chars += ch

take_list = [digits[i] for i in range(len(digits)) if i % 2 == 0]
skip_list = [digits[i] for i in range(len(digits)) if i % 2 != 0]

for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    result += chars[:take]
    chars = chars[take + skip:]

print(result)
