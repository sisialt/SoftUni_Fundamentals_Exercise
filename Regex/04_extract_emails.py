import re

text = input()

pattern = r"(?<=\s)[A-Za-z0-9]([\w.\-]*[A-Za-z0-9])+@[A-Za-z]([A-Za-z-]*[A-Za-z])+(\.[A-Za-z]([A-Za-z-]*[A-Za-z]+))+"
# r"(?<=\s)[A-Za-z\d][A-Za-z\d(\.\-_)?]+@[A-Za-z][A-Za-z(\-)?]+[A-Za-z]\.[A-Za-z]([A-Za-z-]+\.*)*\b"
# (^|\s)([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z0-9\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)

result = re.finditer(pattern, text)

print("\n".join([res[0] for res in result]))


# pattern = r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z0-9\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"
#
# result = re.findall(pattern, text)
#
# print("\n".join([res[0] for res in result]))
