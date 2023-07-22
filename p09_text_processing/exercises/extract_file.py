file_location = input().rsplit("\\", 1)
file_name, file_extension = file_location[1].split(".")
print("File name:", file_name, "\nFile extension:", file_extension)