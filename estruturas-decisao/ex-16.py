def piscininha(x, y, w, h, a, b):
    if x+w > a > x and y+h > b > y:
        print('Dando um tchibum')
    elif (x+w < a or a < x) or (y+h < b or b < y):
        print('Tomando um solzin')
    else:
        print('So com os pezin dentro da agua')
 	