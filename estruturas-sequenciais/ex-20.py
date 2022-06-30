def pacotesDeBolacha(pots, students, eat):
    cookies = pots//students
    maximum = min(cookies, eat) * students
    print(maximum)
