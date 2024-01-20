from re import sub

def simplify_expression(expression):
    # Usuwanie mnożenia przez 1, ale tylko gdy nie wpłynie to na inne części wyrażenia
    expression = sub(r'(?<=\W)1\*', '', expression)
    expression = sub(r'\*1(?=\W|$)', '', expression)

    # Usuwanie dzielenia przez 1
    expression = sub(r'/1(?=\W|$)', '', expression)

    # Usuwanie odejmowania 0, ale tylko gdy nie wpłynie to na inne części wyrażenia
    expression = sub(r'-0(?=\W|$)', '', expression)

    # Usuwanie dodawania 0, ale tylko gdy nie wpłynie to na inne części wyrażenia
    expression = sub(r'\+0(?=\W|$)', '', expression)
    expression = sub(r'(?<=\W)0\+', '', expression)

    # Usuwanie ewentualnych zbędnych plusów na początku
    if expression.startswith('+'):
        expression = expression[1:]

    return expression