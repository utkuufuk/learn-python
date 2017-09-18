import json

# FILES
myFile = open('sample.txt', 'w')
myFile.write("Hey now brown cow\n")
myFile.write("Hey now brown cow\n")
myFile.write("Hey now brown cow\n")
myFile.close();

myFile = open('sample.txt', 'r')
line = myFile.read()
myFile.close()
print(line) 

# 'with' keyword closes the file once access to it is no longer needed
# file is opened in read-only mode by default
with open("sample.txt") as file_object:
    contents = file_object.read()
    print(contents)

# print contents line by line
with open("sample.txt") as file_object:
    for line in file_object:
        print(line)

# JSON
numbers_to_store = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

# store the list object into a json file
with open(filename, 'w') as file_object:
    json.dump(numbers_to_store, file_object)

# load the previously stored list object
with open(filename) as file_object:
    loaded_numbers = json.load(file_object)

print(loaded_numbers)
