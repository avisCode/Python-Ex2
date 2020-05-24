def pentaNumRange(n1, n2):
    def getPentaNum(n): return (n*(3*n-1))/2
    l = []
    for i in range(n1, n2):
        l.append(getPentaNum(i))
    return l


def pentaNumbers():
    first_num = int(input('Enter the first number : '))
    last_num = int(input('Enter the last number : '))
    for i, j in enumerate(pentaNumRange(first_num, last_num)):
        print(j, end=' ')
        if((i+1) % 10 == 0):
            print()
