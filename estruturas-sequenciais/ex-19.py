def pacotesDeBolacha(pots, students, eat):
    cookies = pots//students
    employee = pots - min(cookies, eat) * students
    print(employee)
