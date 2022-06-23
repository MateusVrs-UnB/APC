a, b, c = map(int, input().split())

def age(number):
    year =  number//360
    month = (number-year*360)//30
    days = number-(year*360+month*30)
    print(f'{year} ano(s), {month} mes(es) e {days} dia(s)')

for days in [a, b, c]:
    age(days)
