import re

text = input()

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

cool_threshold = 0
cool_emojis = []
valid_emojis = []

matches = re.finditer(pattern, text)
digits = re.findall(r"\d", text)

if digits:
    cool_threshold = 1
    for digit in digits:
        cool_threshold *= int(digit)

for match in matches:
    valid_emoji = match.group(2)
    valid_emojis.append(valid_emoji)

    coolness = sum([ord(ch) for ch in valid_emoji])
    if coolness >= cool_threshold:
        cool_emojis.append(match.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))
