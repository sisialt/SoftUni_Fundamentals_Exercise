import re

line = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

full_name = re.findall(pattern, line)
print(*full_name)
