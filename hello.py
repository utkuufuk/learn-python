# MATH
print(18 / 4)                          # compute result in float
print(18 // 4)                         # compute result in integer
print(5 ** 3)                          # 5 to the power of 3

# STRINGS
print("double")
print('single')
print(r'print \nstring as is')         # 'r' stands for 'raw'

firstName = 'Utku '
lastName = "Ufuk"
print(firstName + lastName)            # concatanate strings
print(firstName * 3)                   # print firstName 3 times
print(len(lastName))                   # print string length

str(9)                                 # convert number to string

# FILES
myFile = open('sample.txt', 'w')
myFile.write("Hey now brown cow\n")
myFile.close();

myFile = open('sample.txt', 'r')
line = myFile.read()
myFile.close()
print(line) 
