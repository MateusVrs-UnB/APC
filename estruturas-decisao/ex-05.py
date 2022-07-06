def dinheiros(n, a, b):
    two = n//2
    minimum = min((two*b)+((n-two*2)*a), n*a)
    print(minimum)
