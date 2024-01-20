from math import sin, cos, log, exp, tan


def calka_num(funkcja, a, b):
    funkcja = funkcja.replace('^', '**')
    dokladnosc = 10**5
    calka = 0
    przedzial = (b-a)/dokladnosc
    x = a + przedzial/2
    for i in range(dokladnosc):
        wartosc = eval(funkcja)
        calka += wartosc*przedzial
        x += przedzial
    return calka
