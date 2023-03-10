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
