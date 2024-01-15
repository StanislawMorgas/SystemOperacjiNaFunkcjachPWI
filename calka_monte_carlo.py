import random, math 
from sympy import *

def minmax(funkcja,a,b):
    x = symbols('x')
    wyrazenie = sympify(funkcja)
    x_first = a
    x_last = b
    pochodna = diff(funkcja, x)
    kres_a = wyrazenie.subs(x, x_first)
    kres_b = wyrazenie.subs(x, x_last)
    punkty_krytyczne = [kres_b, kres_a]
    miejsca_zerowe_pochodnej = solve(pochodna, x)
    for i in miejsca_zerowe_pochodnej:
        if i<=b and i>=a:
            punkty_krytyczne.append(wyrazenie.subs(x, i))
    maximum = max(punkty_krytyczne)
    minimum = min(punkty_krytyczne)
    return (minimum, maximum)

def calka_monte_carlo(funkcja, a, b):
    minimum = minmax(funkcja,a,b)[0]
    maximum = minmax(funkcja,a,b)[1]
    if minimum > 0:
        minimum = 0
    x = symbols('x')
    cnt = 0
    wyrazenie = sympify(funkcja)
    przybliżenie = 10**4
    for i in range(przybliżenie):
        x_p = random.uniform(a,b)
        y_p = random.uniform(minimum, maximum)
        if y_p <= wyrazenie.subs(x,x_p):
            cnt+=1
    posibility = cnt/przybliżenie
    pole = (maximum-minimum) *(b-a)
    calka = posibility * pole
    return calka
        
print(calka_monte_carlo('sin(x)',2,5))
