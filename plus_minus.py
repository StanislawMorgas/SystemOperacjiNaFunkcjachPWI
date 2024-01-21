from re import sub


def add_minus(fcja):
    fcja = fcja.replace(" ", "")
    fcja = sub(r"\+\(-(.+?)\)", r"-\1", fcja)
    return fcja