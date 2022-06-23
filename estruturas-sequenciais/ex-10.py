a, b, c = map(int, input().split())

def age(number):
    A =  number//360
    M = (number-A*360)//30
    D = number-(A*360+M*30)
    print(f'{A} {M} {D}')

for days in [a, b, c]:
    age(days)
