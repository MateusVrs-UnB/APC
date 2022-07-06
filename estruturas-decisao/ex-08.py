def triangleType(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if len(set([a, b, c])) == 3:
            return 'triangulo escaleno'
        elif len(set([a, b, c])) == 2:
            return 'triangulo isosceles'
        else:
            return 'triangulo equilatero'
    return False

def squareOrReactangle(a, b):
    if a == b:
        return 'quadrado'
    return 'retangulo'

def formamisteriosa(a, b, c):
    print(f'pode ser {squareOrReactangle(a, b)}')
    triangle = triangleType(a, b, c)
    print(f'pode ser {triangle}') if triangle else None
