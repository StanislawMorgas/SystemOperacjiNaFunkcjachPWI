from re import sub


def add_minus(fcja):
    fcja = sub(r'\+\(-(\d+)\)', r'-\1', fcja)
    fcja = sub(r'\+\(-(\d+\.\d+)\)', r'-\1', fcja)
    fcja = sub(r'\+\(-x\)', '-x', fcja)
    return fcja
