def concatenar(first, second):
    print(first+second)

def repetir(first, number):
    print(first*number)

def ambos(first, second, number):
    print((first+second)*number)

first, second, number = input().split()
concatenar(first, second)
repetir(first, int(number))
ambos(first, second, int(number))
