from re import sub, findall, compile


def simple_mult(fcja):
    fcja = fcja.replace(" ", "")

    def mult_el(match):
        match_tab = findall(r"sin\(.+?\)|cos\(.+?\)|x\^-?\d+|x|\d+\.\d+|\d+", match.group(0))
        res_n = 1
        x_power = 0
        x_sign = "+"
        rest = ""
        for n in match_tab:
            if "sin" in n or "cos" in n:
                rest = rest + "*" + n
            elif "x" in n:
                if "^" in n:
                    temp_1 = findall(r"\^(-?\d+)", n)
                    temp_power = temp_1[0]
                    x_power += int(temp_power)
                else:
                    x_power += 1
                temp_2 = findall(r"^([+-])?x", n)
                if temp_2[0] == "+" or temp_2[0] == "":
                    temp_sign = "+"
                else:
                    temp_sign = "-"
                if temp_sign == "-":
                    if x_sign == "+":
                        x_sign = "-"
                    elif x_sign == "-":
                        x_sign = "+"
            elif "." in n:
                res_n *= float(n)
            else:
                res_n *= int(n)

        # iloraz rowny 0
        if res_n == 0:
            return ""
        if res_n > 0:
            n_sign = "+"
            res_n = str(res_n)
        else:
            n_sign = "-"
            res_n = str(res_n)[1:]
        # nie ma x
        if x_power == 0:
            return n_sign + res_n + rest
        # jest x
        else:
            if x_power == 1:
                res_x = "x"
            else:
                res_x = f"x^{x_power}"
        if x_sign == "+" and n_sign == "+" or n_sign == "-" and x_sign == "-":
            return "+" + res_n + "*" + res_x + rest
        else:
            return "-" + res_n + "*" + res_x + rest

    pattern_1 = compile(
        r"(\(?[+-]?(?:sin\(.+?\)|cos\(.+?\)|x\^-?\d+|x|\d+\.\d+|\d+)\)?)(?:\s*\*\s*(\(?[+-]?(?:sin\(.+?\)|cos\(.+?\)|x\^-?\d+|x|\d+\.\d+|\d+)\)?))+")
    fcja = sub(pattern_1, mult_el, fcja)
    fcja = sub(r"\*1(?:\*?)|(?:\*?)1\*", "", fcja)
    while fcja[0] in set(["+", "*", "-", "/"]):
        fcja = fcja[1:]
    while fcja[len(fcja) - 1] in set(["+", "*", "-", "/"]):
        fcja = fcja[:len(fcja) - 1]
    return fcja

