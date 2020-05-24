from eratosthenes import *


def twinp(n):
    l1 = napa(n)
    l2 = l1[:]
    l2.pop(0)
    l2.append(-100)
    dic = dict(zip(l1, l2))
    return list(map(lambda x: {x: x+2}, filter(lambda x: dic[x]-x == 2, dic)))


def printTwinp():
    x = int(input('Enter a number: '))
    print(twinp(x))
