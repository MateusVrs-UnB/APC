def anobissexto(ano):
    if not ano % 400:
        return 'Sim'
    if not ano % 100:
        return 'Nao'
    if not ano % 4:
        return 'Sim'
    return 'Nao'