path_to_file = input()
reverse_path = path_to_file[::-1]
file_name = ''

for el in reverse_path:
    if ord(el) == 92:
        break
    else:
        file_name += el
file_name = file_name[::-1].split(".")
print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[1]}")
