def area(a, b, shape):
    if shape == "retangulo":
        print(f"O retangulo tem {int(a*b)} de area")
    elif shape == "losango" or shape == "triangulo":
        print(f"O {shape} tem {int(a*b/2)} de area") 
    else:
        print(f"O circulo tem {int(b*a**2)} de area") 
