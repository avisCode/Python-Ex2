from Qu3 import reverseNum1


def isPalindrome(n):
    return str(n) == str(reverseNum1(n))


def printIsPalindrome():
    x = int(input("Enter a number: "))
    print("it is a polindrom") if isPalindrome(
        x) else print("it is not polindrom")
