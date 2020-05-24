import math
from functools import reduce


def helpFunc1(n):
    if n == 0:
        return []
    return[(lambda x: math.pow((-1), x+1)/(2*x-1))(n)]+helpFunc1(n-1)


def helpFunc2(n):
    if n == 0:
        return
    print(pi(n), n)
    helpFunc2(n-1)


def pi(n):
    return 4*sum(helpFunc1(n))


def printPiAndI():
    a = int(input('Enter a number: '))
    helpFunc2(a)
