# Pyhton file handling

import os

file_path = "Files/text.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("This is a file")
    else:
        print("The file doesn't exist")
else:
    print("The location doesn't exists")

## Writing files

import json
import csv

txt_data = "I'm learning Python!"

emp = {
    "name" : "Rithvik",
    "age" : 30 ,
    "job" : "Trainee"
}

file_path = "Files/output.txt"
file2 = "Files/employee.json"

try:
    with open(file_path, "w") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")

    with open(file2, "w") as file:
        json.dump(emp, file)
        print(f"json file '{file2}' was created")

except FileExistsError:
    print("The file already exists")

## Reading File

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

    with open(file2, "r") as file:  
        content = json.load(file)
        print(content["name"])
        print(content["age"])

except FileNotFoundError:
    print("The file was not found")    
