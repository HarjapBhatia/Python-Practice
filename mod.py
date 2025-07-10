import math

def checkEven(fr, to) -> list:
    res = []
    for i in range(fr,to+1):
        if i%2 == 0:
            res.append(i)
    return res


def checkPrime(fr, to) -> list:
    primeList = []
    if fr==0 or fr == 1:
        fr == 2
    for i in range(fr, to+1):
        check = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i%j == 0:
                check = False
                break
        if(check): primeList.append(i)
    return primeList


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
