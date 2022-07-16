def soma_harmonica(number):
    if number == 1:
        return 1
    else:
        return 1/number + soma_harmonica(number - 1)
