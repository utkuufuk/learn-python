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

# MAP
income = [10, 30, 75]

def doubleMoney(dollars):
    return dollars * 2

newIncome = list(map(doubleMoney, income))
print(newIncome)
