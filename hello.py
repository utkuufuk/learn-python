# MATH
print(18 / 4)                               # compute result in float
print(18 // 4)                              # compute result in integer
print(5 ** 3)                               # 5 to the power of 3

# STRINGS
print("double")
print('single')
print(r'print \nstring as is')              # 'r' stands for 'raw'

firstName = 'Utku '
lastName = "Ufuk"
print(firstName + lastName)                 # concatanate strings
print(firstName * 3)                        # print firstName 3 times
print(len(lastName))                        # print string length

str(9)                                      # convert number to string

# FUNCTIONS
def beef():
    print("Damn, functions are cool!")

beef()

# function with arguments and return value
def bitcoinToUsd(btc):
    usd = btc * 527
    return usd

usd = bitcoinToUsd(3.8)
print(usd) 

# function with default arguments
def printSentence(subj='Utku', verb='ate', obj='cheese'):
    print(subj, verb, obj)

printSentence()                             # use default arguments
printSentence('Sally', 'farts', 'gently')   # pass custom arguments
printSentence(obj='awesome', verb='is')     # pass 2 arguments in arbitrary order

# function with flexible number of arguments
def addNumbers(*args):
    total = 0;
    for a in args:
        total += a
    print(total)

addNumbers(1, 2)
addNumbers(3, 4, 5)

# SETS
groceries = {"cereal", "milk", "lotion"}
    
if 'milk' in groceries:
    print("You already have milk hoss!")

# DICTIONARIES (Map in Java)
classmates = {"Tony":"cool but smells",
              "Emma":"she sits behind me",
              "Lucy":"asks too many questions"}

print(classmates)                           # print the whole dictionary
classmates['Ogeday'] = "plays ping pong"    # add new key-value pair to the dictionary
del classmates['Ogeday']                    # remove the key-value pair from the dictionaryy
print(classmates['Emma'])                   # print the value for key 'Emma'
print(classmates.get('Melahat', "No idea")) # return default value if key does not exist

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

# FILES
myFile = open('sample.txt', 'w')
myFile.write("Hey now brown cow\n")
myFile.close();

myFile = open('sample.txt', 'r')
line = myFile.read()
myFile.close()
print(line) 

# MAP
income = [10, 30, 75]

def doubleMoney(dollars):
    return dollars * 2

newIncome = list(map(doubleMoney, income))
print(newIncome)

