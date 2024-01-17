from re import sub, findall


def simple_mult(fcja):
    def mult_el(match):
        num = findall(r'-?\d+\.\d+|\d+', match.group(0))
        res = 1
        for n in num:
            if "." in n:
                res *= float(n)
            else:
                res *= int(n)
        if res >= 0:
            return "+" + str(res)
        else:
            return str(res)

    fcja = sub(r'(\(?[+-]?(?:\d+\.\d+|\d+)\)?)(?:\s*\*\s*(\(?[+-]?(?:\d+\.\d+|\d+)\)?))+', mult_el, fcja)
    if fcja[0] == "+" or fcja[0] == "*":
        fcja = fcja[1:]
    return fcja
