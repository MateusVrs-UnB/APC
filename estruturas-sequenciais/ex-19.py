def pacotesDeBolacha(pots, students, eat):
    array = list()
    for number in range(eat, -1, -1):
        rest = pots-(students*number)
        if rest >= 0:
            array.append(rest)
    print(min(array))
