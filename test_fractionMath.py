import io
import sys
import fractionMath

# ** (thanks to paxdiablo on stackoverflow for starting code for capturing terminal output)

green = '\033[32m'
gray = '\033[37m'
purple = '\033[35m'

def testConsoleOutput(stringIn, stringOutArray, passMsg=""):
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput(stringIn)               # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == '\n'.join(stringOutArray).strip(), 'input: '+stringIn+'\n\nexpected output:\n\n'+'\n'.join(stringOutArray).strip()+'\n\nactual output:\n\n'+capturedOutput.getvalue().strip()
    if passMsg:
        print(green, f"Pass: {passMsg}", gray)


def test_fractionMath():


    #Helper function validation

    # check for CHARACTER VALIDATION
    print('\nCharacter Validation\n')
    badInput = 'abcdef39y*'
    goodInput = '09_1/3 / 2'
    assert fractionMath.checkCorrectCharacters(badInput) == False, f"checkCorrectCharacters() for {badInput} should return False."
    print(green, f"Pass: Rejects bad input: {badInput}", gray)
    assert fractionMath.checkCorrectCharacters(goodInput) == True, f"checkCorrectCharacters() for {goodInput} should return True."
    print(green, f"Pass: Approves good input: {goodInput}", gray)
    
    # properly converts mixed numbers to improper fractions
    print('\nConverting to Improper Fractions\n')
    negativeInput = '-23_1/2'
    positiveInput = '23_1/2'
    plainFraction = '2/3'
    wholeNumber = '2'
    assert fractionMath.convertMixedToFraction(negativeInput) == '-47/2', f"converting {negativeInput} should yield -47/2"
    print(green, f"Pass: Negative mixed number turns into correct negative fraction: {negativeInput} --> -47/2", gray)
    assert fractionMath.convertMixedToFraction(positiveInput) == '47/2', f"converting {positiveInput} should yield 47/2"
    print(green, f"Pass: Positive mixed number turns into correct positive fraction: {positiveInput} --> 47/2", gray)
    assert fractionMath.convertMixedToFraction(plainFraction) == '2/3', f"converting {plainFraction} should yield 2/3"
    print(green, f"Pass: Plain fraction remains the same: {plainFraction} --> 2/3", gray)
    assert fractionMath.convertMixedToFraction(wholeNumber) == '2/1', f"converting {wholeNumber} should yield 2/1"
    print(green, f"Pass: Whole number turns into improper fraction: {wholeNumber} --> 2/1", gray)

    # helper math functions
    print('\nGCD\n')
    pairs = [[20, 456, 4], [4,12, 4], [4, 8, 4], [21, 49, 7], [3,9, 3], [0, 4, 4], [0, 0, 0], [1, 0, 1]]
    for a,b,c in pairs:
        assert fractionMath.findGCD(a,b) == c, f"The Greatest Common Denominator of {a} and {b} should be {c}"
    print(green, "Pass: GCD all processed successfully", gray)
    

    #Output validation
    print('\nOutput Validation\n')
    # check for HELP ADVICE **
    testConsoleOutput('help', fractionMath.advice, 'Outputs help advice')

    # check for EXIT MESSAGE **
    testConsoleOutput('exit', fractionMath.exitLines, 'Outputs exit message')

    # check for BAD INPUT MESSAGE **
    badInput = 'ksdf 39543 sdf'
    testConsoleOutput(badInput, ["Please use only numbers, _, and allowed operators. Type 'help' for more info!"], "Outputs rejected input message")

    # check for SINGLE WHOLE NUMBER or SINGLE PROPER FRACTION **
    singleWhole = '42'
    singleProper = '1/32'
    testConsoleOutput(singleWhole, ['= 42'], f"Outputs whole number unchanged: 42 --> 42")
    testConsoleOutput(singleProper, ['= 1/32'], f"Outputs single proper fraction unchanged: 1/32 --> 1/32")

    # check for IMPROPER OPERATOR PLACEMENT **
    badInputArray = ['2 * *', '2_1/2 /', '- 3 2/3']
    outputMatch = ["= Please follow the following format: number operator number"]
    for item in badInputArray:
        testConsoleOutput(item, outputMatch, "Rejects improperly placed operators: "+item)
    

    # check for ADDITION
    print('\nAddition Validation\n')
    additionInput = [
        ['325/90 + 140/13', ['= 14_89/234']],
        ['1/2 +   1/3', ['= 5/6']],
        ['30/7 + 2/4    ', ['= 4_11/14']],
        ['1/2 + 1/2', ['= 1']],
        ['1_3/4 + 2_3/8', ['= 4_1/8']],
        ['1_3/4 + 7', ['= 8_3/4']],
        ['-1/2 + 4_2/3', ['= 4_1/6']],
        ['-1/2 + -4_2/3', ['= -5_1/6']],
        ['1/2 + -1/2', ['= 0']]
        ]
    for inputString, outputString in additionInput:
        testConsoleOutput(inputString, outputString, f"{inputString} {outputString[0]}")


# check for SUBTRACTION
    print('\nSubtraction Validation\n')
    additionInput = [
        ['325/90 - 140/13', ['= -7_37/234']],
        ['1/2 -   1/3', ['= 1/6']],
        ['30/7 - 2/4    ', ['= 3_11/14']],
        ['1/2 - 1/2', ['= 0']],
        ['1_3/4 - 2_3/8', ['= -5/8']],
        ['1_3/4 - 7', ['= -5_1/4']],
        ['-1/2 - 4_2/3', ['= -5_1/6']],
        ['-1/2 - -4_2/3', ['= 4_1/6']],
        ['1/2 - -1/2', ['= 1']]
        ]
    for inputString, outputString in additionInput:
        testConsoleOutput(inputString, outputString, f"{inputString} {outputString[0]}")

    # check for MULTIPLICATION
    print('\nMultiplication Validation\n')
    additionInput = [
        ['325/90 * 140/13', ['= 38_8/9']],
        ['1/2 *   1/3', ['= 1/6']],
        ['30/7 * 2/4    ', ['= 2_1/7']],
        ['1/2 * 1/2', ['= 1/4']],
        ['1_3/4 * 2_3/8', ['= 4_5/32']],
        ['1_3/4 * 7', ['= 12_1/4']],
        ['-1/2 * 4_2/3', ['= -2_1/3']],
        ['-1/2 * -4_2/3', ['= 2_1/3']],
        ['1/2 * -1/2', ['= -1/4']]
        ]
    for inputString, outputString in additionInput:
        testConsoleOutput(inputString, outputString, f"{inputString} {outputString[0]}")


    # check for DIVISION
    print('\nDivision Validation\n')
    additionInput = [
        ['325/90 / 140/13', ['= 169/504']],
        ['1/2 /   1/3', ['= 1_1/2']],
        ['30/7 / 2/4    ', ['= 8_4/7']],
        ['1/2 / 1/2', ['= 1']],
        ['1_3/4 / 2_3/8', ['= 14/19']],
        ['1_3/4 / 7', ['= 1/4']],
        ['-1/2 / 4_2/3', ['= -3/28']],
        ['-1/2 / -4_2/3', ['= 3/28']],
        ['1/2 / -1/2', ['= -1']]
        ]
    for inputString, outputString in additionInput:
        testConsoleOutput(inputString, outputString, f"{inputString} {outputString[0]}")

    
if __name__ == "__main__":
    test_fractionMath()
    print('\nFinal Assessment\n')
    print(green, "Passed all tests.\n", gray)