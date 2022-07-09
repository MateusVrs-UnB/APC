def formamisteriosa(a, b, c):
    if a == b:
        print("pode ser quadrado")
    else:
        print("pode ser retangulo")
    if a + b > c and a + c >  b and b + c  > a:
        if a == b and b == c:
            tipo = 'equilatero'
        elif a == b or b == c or c == a:
            tipo = "isosceles"
        else:
            tipo = "escaleno"
        print(f'pode ser triangulo {tipo}')
