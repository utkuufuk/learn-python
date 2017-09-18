# LISTS
numbers = [29, 58, 66, 71, 8]               # initialize a list
newNums = numbers[:]                        # copy the list
newNums = numbers                           # these two variables now point to the same list
squares = [n ** 2 for n in range(1,11)]     # build a list using list comprehension

# accessing elements
print(numbers[-1])                          # print the last character
print(numbers[-3:])                         # print the last 3 characters

# change ordering
numbers.reverse()                           # reverse the order of the list
numbers.sort()                              # sort the numbers in the list
tempNums = sorted(numbers)                  # return a sorted copy of the list

# append & prepend
numbers += [7, 6]                           # append new items to the list
numbers.append(120)                         # another way to append a new item
numbers = [1, 2] + numbers                  # prepend new items to the list

# insert & remove elements
numbers.insert(0, 27)                       # insert a number at the beginning of the list
numbers.remove(66)                          # remove the first occurance of a value from the list
del numbers[0]                              # remove the first number from the list
lastNum = numbers.pop()                     # remove and return the last number
firstNum = numbers.pop(0)                   # remove and return the first number
numbers[:2] = []                            # remove the first 2 items
numbers = []                                # clear the list

# TUPLES
dimensions = (200, 50)                      # tuples are immutable lists
