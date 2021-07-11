import io
import sys
import fractionMath

# ** (thanks to paxdiablo on stackoverflow for starting code for capturing terminal output)

green = '\033[32m'
gray = '\033[37m'
purple = '\033[35m'

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
    assert fractionMath.convertMixedToFraction(negativeInput) == '-47/2', f"converting {negativeInput} should yield -47/2"
    print(green, f"Pass: Negative mixed number turns into correct negative fraction: {negativeInput} --> -47/2", gray)
    assert fractionMath.convertMixedToFraction(positiveInput) == '47/2', f"converting {positiveInput} should yield 47/2"
    print(green, f"Pass: Positive mixed number turns into correct positive fraction: {positiveInput} --> 47/2", gray)



    #Output validation
    print('\nOutput Validation\n')
    # check for HELP ADVICE **
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput('help')                 # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == '\n'.join(fractionMath.advice).strip(), 'Help input returns \n\n' + capturedOutput.getvalue().strip() + '\n\n instead of \n\n' + "\n".join(fractionMath.advice).strip()
    print(green, "Pass: Outputs help advice", gray)

    # check for EXIT MESSAGE **
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput('exit')                 # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == '\n'.join(fractionMath.exitLines).strip(), 'Help input returns \n\n' + capturedOutput.getvalue().strip() + '\n\n instead of \n\n' + "\n".join(fractionMath.exitLines).strip()
    print(green, "Pass: Outputs exit message", gray)

    # check for BAD INPUT MESSAGE **
    badInput = 'ksdf 39543 sdf'
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput(badInput)               # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == "Please use only numbers, _, and allowed operators. Type 'help' for more info!", 'Help input returns \n\n' + capturedOutput.getvalue().strip() + "\n\n instead of \n\n Please use only numbers, _, and allowed operators. Type 'help' for more info!"
    print(green, "Pass: Outputs rejected input message", gray)

    # check for SINGLE WHOLE NUMBER or SINGLE PROPER FRACTION **
    singleWhole = '42'
    singleProper = '1/32'
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput(singleWhole)                 # Call function.
    fractionMath.parseInput(singleProper)                 # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == '= 42\n= 1/32', f"expect output: \n= 42\n= 1/32\nactual output: \n{capturedOutput.getvalue().strip()}"
    print(green, "Pass: Outputs single whole or proper fraction numbers as is", gray)



if __name__ == "__main__":
    test_fractionMath()
    print('\nFinal Assessment\n')
    print(green, "Passed all tests.\n", gray)