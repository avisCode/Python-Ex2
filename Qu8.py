def add3dicts(d1, d2, d3):
    def Tdict(L, acc):
        if(not(L)):
            return acc
        if(L):
            k = L[0]
            if(k in d1):
                if(k in d2):
                    if(k in d3):
                        acc[k] = (d1[k], d2[k], d3[k])
                    else:
                        acc[k] = (d1[k], d2[k])
                elif(k in d3):
                    acc[k] = (d1[k], d3[k])
                else:
                    acc[k] = d1[k]
            elif(k in d2):
                if(k in d3):
                    acc[k] = (d2[k], d3[k])
                else:
                    acc[k] = d2[k]
            else:
                acc[k] = d3[k]
            return Tdict(L[1:], acc)
    L = list(d1)+list(d2)+list(d3)
    return Tdict(L, {})


def printadd3Dictd():
    a = dict(input('Enter the first dict: '))
    b = dict(input('Enter the second dict: '))
    c = dict(input('Enter the therid dict: '))
    print(add3dicts(a, b, c))
