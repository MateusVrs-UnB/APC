def trocarAB(a, b):
    print(b, a)
    
for n in range(5):
    a, b = map(int, input().split())
    trocarAB(a, b)