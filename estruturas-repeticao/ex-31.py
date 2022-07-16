N = int(input())
for n in range(N):
    print(f"{n+1} elefante{'s' if n > 0 else ''} incomoda{'m' if n > 0 else ''} muita gente...")
    print(f"{n+2} elefantes incomodam, {'incomodam, '*n}incomodam muito mais...")

