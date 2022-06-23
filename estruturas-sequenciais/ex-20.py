def pacotesDeBolacha(pots, students, eat):
    array = list()
    for number in range(eat, -1, -1):
        total = (students*number)
        if pots-total >= 0:
            array.append(total)
    print(max(array))
