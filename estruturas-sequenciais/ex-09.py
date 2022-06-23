a, b, c = map(int, input().split())
for n in [a, b, c]:
    year =  n//360
    month = (n-year*360)//30
    days = n-(year*360+month*30)
    print(f'{year} ano(s), {month} mes(es) e {days} dia(s)')
