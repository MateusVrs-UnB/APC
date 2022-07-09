def maravilhosos(number):
    print(int(number))
    while number != 1:
        if not number % 2:
            return maravilhosos(number/2)
        else:
            return maravilhosos(3*number + 1)
            
N = int(input())
maravilhosos(N)
