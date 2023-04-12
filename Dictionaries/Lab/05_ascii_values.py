chars = input().split(", ")

chars_with_ascii = {ch: ord(ch) for ch in chars}
print(chars_with_ascii)