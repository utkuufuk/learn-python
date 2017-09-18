# CONDITIONS
name = "Lucy"
if name is "Lucy":
    print("Hi there Lucy!")
elif name is "Bucky":
    print("What up Bucky?")
else: 
    print("I don't know you.")

# negation
if "x" not in name:
    print("Your name doesn't contain x")

# LOOPS
foods = ['milk', 'eggs', 'tuna', 'meat']
for f in foods:
    print(f)
    
for f in foods[1:]:                         # loop through a portion of the list
    print(f)

for i in range(10):                         # repeat start from 0 to 9
    print(i)

for i in range(5, 12):                      # set i to 5 and repeat until 11
    print(i)

for i in range(10, 100, 5):                 # start from 10, end at 95, increment by 5
    print(i)

for _ in range(10):                         # don't care about the index
    print("i don't care")

count = 0
while count < 10:
    print(count)
    count += 1                              # count++ does not work!

# break
magicNumber = 23

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number")     
        break

# continue
numbersTaken = [2, 5, 12, 17]
print("Here are the available numbers:")

for n in range(1, 20):
    if n in numbersTaken:                   # similar to contains() in Java
        continue
    print(n)
