from re import sub, findall

# funkcja = "2*3*x + 7*1*(-x) + 9*1000*(-7)"
# funkcja = funkcja.replace(" ", "")


def simple_mult(fcja):
    def mult_el(match):
        num = findall(r'-?\d+', match.group(0))
        res = 1
        for n in num:
            res *= int(n)
        return str(res)
    fcja = sub(r'(\(?[+-]?\d+\)?)(?:\s*\*\s*(\(?[+-]?\d+\)?))+', mult_el, fcja)
    return fcja



