import os

directory = "/home/anthony/Desktop/flags/"

def rename_file(file):
    new_file = ""
    for character in file:
        if character == "_":
            new_file = new_file + " "
        elif character == '"':
            character == ""
        else:
            new_file = new_file + character
    return new_file


for filename in os.listdir(directory):
    if "_" in filename or '"' in filename:
        os.rename('/home/anthony/Desktop/flags/' + filename, rename_file(filename)) 



