# SETS
groceries = {"cereal", "milk", "lotion"}
    
if 'milk' in groceries:
    print("You already have milk hoss!")

# DICTIONARIES (Maps in C++ & Java)
classmates = {"Tony":"cool but smells",
              "Emma":"she sits behind me",
              "Lucy":"asks too many questions"}

print(classmates)                           # print the whole dictionary
classmates['Robert'] = "plays ping pong"    # add new key-value pair to the dictionary
del classmates['Robert']                    # remove the key-value pair from the dictionaryy
print(classmates['Emma'])                   # print the value for key 'Emma'
print(classmates.get('Jane', "No idea"))    # return default value if key does not exist

for k, v in classmates.items():             # iterate over key-value pairs
    print(k, v)

for name in classmates:                     # iterate over keys
    print(name)

for key in sorted(classmates.keys()):       # iterate over sorted keys
    print(key)

for value in classmates.values():           # iterate over values 
    print(value)

for value in set(classmates.values()):      # iterate over unique values
    print(value)


