from math import hypot
def classificador(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print('triangulo')
        if len(set([a, b, c])) == 3:
            print('escaleno')
        if len(set([a, b, c])) <= 2:
            print('isosceles')
        if len(set([a, b, c])) == 1:
            print('equilatero')

        if hypot(*sorted([a, b, c])[:2]) == max([a, b, c]):
            print('retangulo')
        
    else:
        print('gondim sendo gondim')

