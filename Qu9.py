from Qu1 import pentaNumbers
from Qu2 import printSumDigits
from Qu3 import printReverse
from Qu4 import printIsPalindrome
from Qu5 import printNumberAndFuncM
from Qu6 import printPiAndI
from Qu7 import printTwinp
from Qu8 import printadd3Dictd

# printing the menu options


def prtMenu(shapes):
    for i in range(len(shapes)):
        print(i+1, shapes[i])
    return


#
# main program
#
print("Welcome to the program")
print("---------------------------------------")
# Print out the menu
options = ("print penta numbers between 2 numbers", "print the sum of Digits of a number", "print the revers of a number",
           "Checkes if a number is a Palindrome", "printing a sires", "printing the number neer PI", "print Twinp numbers", "dicts func")
while True:
    print("\n\nPlease select a options (press 0 to quit):")
    prtMenu(options)
    # Get the user's choice:
    option = input(">: ")
    # Calculate the area:
    if option == "1":
        pentaNumbers()
        continue
    elif option == "2":
        printSumDigits()
        continue
    elif option == "3":
        printReverse()
        continue
    elif option == "4":
        printIsPalindrome()
        continue
    elif option == "5":
        printNumberAndFuncM()
        continue
    elif option == "6":
        printPiAndI()
        continue
    elif option == "7":
        printTwinp()
        continue
    elif option == "8":
        printadd3Dictd()()
        continue
    else:
        print("Invalid shape")
