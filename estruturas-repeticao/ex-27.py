from math import sqrt
def ehPrimo(number):
    for n in range(2, int(sqrt(number)) + 1):
        if not number % n:
            return 0
    return 1

def divisoresPrimos(number):
    result = 0
    for n in range(2, number//2 + 1):
        if not number % n and ehPrimo(n):
            result += 1
    return result
