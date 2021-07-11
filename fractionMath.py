import re

# VARIABLES

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
numberParts = [x for x in '0123456789_/']



# MAIN FUNCTION

def fractionMath():
    '''a simple fraction math program intended to give an answer formatted as a fraction to fractions being added, subtracted, multiplied, or divided'''
    print("Welcome to Fraction Math. For help, enter 'help'. Otherwise, let's do math!")
    goAgain = True
    while goAgain:
        userInput = input("? ")
        goAgain = parseInput(userInput)





# SUB FUNCTIONS

# standard Euclidean Algorithm
def findGCD(num1, num2):
    '''return the greatest common denominator for two numbers'''
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1


def convertMixedToFraction(number):
    # temporarily remove minus sign so we can parse the string into numbers
    negative = number[0] == "-"
    number = number[1:] if negative else number
    # consolidate mixed numbers into a single fraction
    if '_' in number:
        whole, fraction = number.split("_")
        numerator, denominator = fraction.split("/")
        improperFraction = f'{int(numerator)+(int(whole)*int(denominator))}/{denominator}'
        return '-' + improperFraction if negative else improperFraction
    # send plain fractions on as is
    elif '/' in number:
        return number
    # turn whole numbers into fractions as well.
    else:
        return f"-{number}/1" if negative else f"{number}/1"

def convertFractionToProper(numArray):
    '''function to ensure that improper fractions are turned into proper fractions for final display'''
    numerator = numArray[0]
    denominator = numArray[1]
    # simplify improper fractions into mixed numbers
    if numerator > denominator:
        whole = 0
        while numerator > denominator-1:
            whole += 1
            numerator -= denominator
        gcd = findGCD(numerator, denominator)
        return f"{whole}_{int(numerator/gcd)}/{int(denominator/gcd)}"
    # ensure that fractions are shown with the smallest possible denominator
    elif numerator < denominator:
        gcd = findGCD(numerator, denominator)
        return f"{int(numerator/gcd)}/{int(denominator/gcd)}"
    # return 1 for fractions that have equal numerator and denominator
    else:
        return '1'


def doTheMath(userInput):
    mathArray = userInput.split()
    if not any([x in operators for x in mathArray]):
        # necessary task = turn improper fractions into correct form
        return mathArray[0] if len(mathArray) == 1 else "You must include an operator to combine multiple numbers"
    # let's get it working for single operators first
    # check operator placement and length of arguments
    if not len(mathArray) == 3 or mathArray[1] not in operators or mathArray[0] in operators or mathArray[2] in operators:
        return 'Please follow the following format: number operator number'
    else:
        # check number format
        firstNum, operator, secondNum = mathArray
        firstMatch = re.match("[\d]+_[\d]+/[\d]+|[\d]+/[\d]+|[\d]+", firstNum)
        secondMatch = re.match("[\d]+_[\d]+/[\d]+|[\d]+/[\d]+|[\d]+", secondNum)
        if not firstMatch or firstMatch.group(0) != firstNum:
            return f"{firstNum} does not match expected number format. Type 'help' for more information!"
        elif not secondMatch or secondMatch.group(0) != secondNum:
            return f"{secondNum} does not match expected number format. Type 'help' for more information!"
        else:
            # convert numbers to improper fractions
            firstNum = convertMixedToFraction(firstNum).split('/')
            secondNum = convertMixedToFraction(secondNum).split('/')
            if operator == "+":
                # return firstNum, operator, secondNum
                if (firstNum[1] == secondNum[1]):
                    initialTotal = [int(firstNum[0]) + int(secondNum[0]), int(firstNum[1])]
                    return convertFractionToProper(initialTotal)
                else:
                    # ensure matching denominators
                    matchedFirstNum = [int(firstNum[0])*int(secondNum[1]), int(firstNum[1])*int(secondNum[1])]
                    matchedSecondNum = [int(secondNum[0])*int(firstNum[1]), int(secondNum[1])*int(firstNum[1])]
                    initialTotal = [matchedFirstNum[0]+matchedSecondNum[0], matchedFirstNum[1]]
                    return convertFractionToProper(initialTotal)



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