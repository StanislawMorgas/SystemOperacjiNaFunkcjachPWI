from math import sin, cos, log, exp, tan


def calka_num(funkcja, a, b):
    dokladnosc = 10**5
    calka = 0
    przedzial = (b-a)/dokladnosc
    x = a
    for i in range(dokladnosc):
        wartosc = eval(funkcja)
        calka += wartosc*przedzial
        x += przedzial
    return calka
