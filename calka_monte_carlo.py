import random 
from sympy import symbols, sympify,diff

def calka_monte_carlo(funkcja, a, b):
    x = symbols('x')
    wyrazenie = sympify(funkcja)
    x_value = a
    wynik = wyrazenie.subs(x, x_value)
    pochodna = diff(funkcja, x)
    return wynik, pochodna

print(calka_monte_carlo('5*x**2 - 3*x + 2',2,5))
