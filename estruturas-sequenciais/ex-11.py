def peso_ideal(height):
    male = 72.7 * height - 58
    female =  62.1 * height - 44.7
    print(str(round(male, 2)).ljust(5, '0'), str(round(female, 2)).ljust(5, '0'))

height = float(input())
peso_ideal(height)