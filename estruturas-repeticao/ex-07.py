dollar = float(input())
value = int(input())
times = int(input())
for time in range(1, times+1):
    print(f'Lote: {time} - Total da venda: R$ {dollar*value*1.025:.2f}')