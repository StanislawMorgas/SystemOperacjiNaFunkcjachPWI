import random 
from sympy import *

def calka_monte_carlo(funkcja, a, b):
    x = symbols('x')
    wyrazenie = sympify(funkcja)
    x_first = a
    x_last = b
    pochodna = diff(funkcja, x)
    kres_a = wyrazenie.subs(x, x_first)
    kres_b = wyrazenie.subs(x, x_last)
    punkty_krytyczne = [kres_a, kres_b]
    miejsca_zerowe_pochodnej = solve(pochodna, x)
    for i in miejsca_zerowe_pochodnej:
        punkty_krytyczne.append(wyrazenie.subs(x, i))
    max = max(punkty_krytyczne)
    min = min(punkty_krytyczne)
    


    return (miejsca_zerowe_pochodnej, pochodna)

print(calka_monte_carlo('5*x**2 - 3*x + 2',2,5))
