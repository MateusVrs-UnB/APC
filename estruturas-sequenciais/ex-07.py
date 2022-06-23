def maiorAB(a, b):
    print(max(a, b))

for n in range(5):
    a, b = map(int, input().split())
    maiorAB(a, b)