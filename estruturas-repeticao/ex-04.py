N = int(input())
for time in range(N):
    array = map(float, input().split())
    average = sum(array)/3
    if average >= 7:
        print(f'O ALUNO {time} FOI APROVADO')
    else:
        print(f'O ALUNO {time} FOI REPROVADO')
