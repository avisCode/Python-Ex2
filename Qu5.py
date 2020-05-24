def helpFunc1(n):
    if n == 1:
        return [0.5]
    return [(lambda x:x/(x+1))(n)]+helpFunc1(n-1)


def helpFunc2(n):
    if n == 0:
        return
    print(n, m(n))
    helpFunc2(n-1)


def m(n):
    return sum(helpFunc1(n))


def printNumberAndFuncM():
    x = int(input('Enter number: '))
    helpFunc2(x)
