def banner(number):
    if number > 0:
        if not number % 2:
            print("| | | | | | | | | |")
        else:
            print("- - - - - - - - - -")
    else:
        if not number % 2:
            print(". . . . . . . . . .")
        else:
            print("= = = = = = = = = =")
    