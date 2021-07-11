# variables

advice = [
            "",
            "HELP:", 
            "",
            "Fraction Math is a simple program designed to take operations on fractions as an input and produce a fractional result.", 
            "Legal operators are *, /, +, - (multiply, divide, add, subtract).",
            "Operands and operators may be separated by one or more spaces.",
            "Mixed numbers may be represended in the following format: whole_numerator/denominator (3_1/4).",
            "Improper fractions and whole numbers are also allowed as operands.",
            "You may exit at any time by inputting 'exit'.",
            "",
            "",
            ]
exitLines = [
    '',
    'Thanks for using Fraction Math!',
    ''
    ]
colors = {
    'red': '\003[08',
    'cyan': '\033[36m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'gray': '\033[37m',
    'yellow': '\033[93m',
    'purple': '\033[35m'
}
operators = ['*', '/', "-", '+']



#main function

def fractionMath():
    '''a simple fraction math program intended to give an answer formatted as a fraction to fractions being added, subtracted, multiplied, or divided'''
    print("Welcome to Fraction Math. For help, enter 'help'. Otherwise, let's do math!")
    goAgain = True
    while goAgain:
        userInput = input("? ")
        goAgain = parseInput(userInput)





#sub functions

def convertMixedToFraction(number):
    negative = number[0] == "-"
    number = number[1:] if negative else number
    whole, fraction = number.split("_")
    numerator, denominator = fraction.split("/")
    improperFraction = f'{int(numerator)+(int(whole)*int(denominator))}/{denominator}'
    return '-' + improperFraction if negative else improperFraction

def doTheMath(userInput):
    mathArray = userInput.split()
    if not any([x in operators for x in mathArray]):
        # necessary task = turn improper fractions into correct form
        return mathArray[0] if len(mathArray) == 1 else "You must include an operator to combine multiple numbers"
    #let's get it working for single operators first
        return 'operators present'

def checkCorrectCharacters(userInput):
    allowedCharacters = [x for x in '0123456789_/*-+= ']
    for char in userInput:
        if char not in allowedCharacters:
            return False
    return True

def parseInput(userInput):
    if (userInput.lower() == 'help'):
        print('\n'.join(advice))
        return True
    elif (userInput.lower() == 'exit' or userInput.lower() == 'quit' ):
        print('\n'.join(exitLines))
        return False
    elif (checkCorrectCharacters(userInput)):
        answer = doTheMath(userInput)
        print(f'= {answer}')
        return True
    else:
        print("Please use only numbers, _, and allowed operators. Type 'help' for more info!")
        return True


# run script

if __name__ == '__main__':
    fractionMath()