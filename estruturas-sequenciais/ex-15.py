def qualPeriodo(semester, year, digit):
    total = 2*(year - int('20'+str(semester)[:2]))
    print(total-int(str(semester)[3])+digit+1)
