path_to_file = input()
index_of_dot = 0
file_name = ""
extension = ""

for i in range(-1, -len(path_to_file), -1):
    if path_to_file[i] == ".":
        index_of_dot = i
        extension = path_to_file[i + 1:]
    elif path_to_file[i] == "\\":
        file_name = path_to_file[i + 1:index_of_dot]
        break

print(f"File name: {file_name}\nFile extension: {extension}")

# with file_name, that includes "."
# for i in range(-1, -len(path_to_file), -1):
#     if path_to_file[i] == ".":
#         index_of_dot = i
#         extension = path_to_file[i + 1:]
#         break
#
# for i in range(-1, -len(path_to_file), -1):
#     if path_to_file[i] == "\\":
#         file_name = path_to_file[i + 1:index_of_dot]
#         break

# path_to_file = input()
# path_file_args = path_to_file.split("\\")
# file_name_with_extension = path_file_args[-1]
#
# file_name = file_name_with_extension.split(".")
# extension = file_name.pop()
# print(f"File name: {'.'.join(file_name)}\nFile extension: {extension}")
