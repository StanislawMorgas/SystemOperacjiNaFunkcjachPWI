from re import sub

def simplify_expression(expression):
    expression = sub(r'(?<=\W)1\*', '', expression)
    expression = sub(r'\*1(?=\W|$)', '', expression)

    expression = sub(r'/1(?=\W|$)', '', expression)

    expression = sub(r'-0(?=\W|$)', '', expression)

    expression = sub(r'\+0(?=\W|$)', '', expression)
    expression = sub(r'(?<=\W)0\+', '', expression)

    if expression.startswith('+'):
        expression = expression[1:]

    return expression