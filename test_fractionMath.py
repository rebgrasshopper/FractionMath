import io
import sys
import fractionMath


def test_fractionMath():

    # check for character validation
    badInput = 'abcdef39y*'
    goodInput = '09_1/3 / 2'
    assert fractionMath.checkCorrectCharacters(badInput) == False, f"checkCorrectCharacters() for {badInput} should return False."
    print('\033[32m', f"Pass: Rejects bad input: {badInput}", '\033[37m')
    assert fractionMath.checkCorrectCharacters(goodInput) == True, f"checkCorrectCharacters() for {goodInput} should return True."
    print('\033[32m', f"Pass: Approves good input: {goodInput}", '\033[37m')
    

    # check for help advice, thanks to paxdiablo on stackoverflow for starting code for capturing terminal output
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # Redirect stdout.
    fractionMath.parseInput('help')                 # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue().strip() == '\n'.join(fractionMath.advice).strip(), 'Help input returns \n\n' + capturedOutput.getvalue().strip() + '\n\n instead of \n\n' + "\n".join(fractionMath.advice).strip()
    print('\033[32m', "Pass: Outputs help advice", '\033[37m')



if __name__ == "__main__":
    test_fractionMath()
    print('')
    print('\033[32m', "Everything passed", '\033[37m')