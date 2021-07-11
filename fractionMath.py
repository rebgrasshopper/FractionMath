def doTheMath(num1, num2):
    return num1 + num2

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

colors = {
    'red': '\003[08',
    'cyan': '\033[36m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'gray': '\033[37m',
    'yellow': '\033[93m',
    'purple': '\033[35m'
}

def fractionMath():
    '''a simple fraction math program intended to give an answer formatted as a fraction to fractions being added, subtracted, multiplied, or divided'''
    print("Welcome to Fraction Math. For help, enter 'help'. Otherwise, let's do math!")
    goAgain = True
    while goAgain:
        userInput = input("? ")
        goAgain = parseInput(userInput)

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
        exitLines = ['','Thanks for using Fraction Math!', '']
        print(*exitLines, sep = "\n")
        return False
    elif (checkCorrectCharacters(userInput)):
        answer = doTheMath(1, 2)
        print(colors['purple'], f'= {answer}.', colors['gray'])
        return True
    else:
        print("Please use only numbers, _, and allowed operators. Type 'help' for more info!")
        return True




if __name__ == '__main__':
    fractionMath()