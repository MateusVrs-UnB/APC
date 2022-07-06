from math import ceil
def qtdcopos(number):
    if not number % 4 and number != 0:
        print('Pode levar pros calourinhos, deivis!')
    else:
        print(f'Pode voltar pro ceubinho, deivis! Falta(m) {ceil((number+1)/4)*4 - number} copo(s)!')
