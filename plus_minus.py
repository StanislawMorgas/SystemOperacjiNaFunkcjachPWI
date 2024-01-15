from re import sub

funkcja = "2*x + (-x) + (-7)"
funkcja = funkcja.replace(" ", "")


def add_minus(fcja):
    fcja = sub(r'\+\(-(\d+)\)', r'-\1', fcja)
    fcja = sub(r'\+\(-x\)', '-x', fcja)
    return fcja


