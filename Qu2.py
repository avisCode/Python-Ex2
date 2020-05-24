def sumDigits1(n):
    return sum(helpFunc1(n))


def helpFunc1(n):
    if n == 0:
        return []
    return [n % 10] + helpFunc1(n//10)


def sumDigits2(n):
    return sum(helpFunc2(n))


def helpFunc2(n):
    l = []
    for i in str(n):
        l.append(int(i))
    return l


def printSumDigits():
    x = int(input("Enter the first number: "))
    print(sumDigits1(x))
    print(sumDigits2(x))
