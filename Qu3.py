from Qu2 import helpFunc2


def reverseNum1(n):
    return int(str(n)[::-1])


def reverseNum2(n):
    l = list(reversed(helpFunc2(n)))
    for i in range(len(l)):
        l[i] = str(l[i])
    return int("".join(l))


def printReverse():
    x = int(input('Enter a number: '))
    print(reverseNum1(x))
    print(reverseNum2(x))
