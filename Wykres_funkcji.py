# %%
import numpy as np
from numpy import cos, sin, log, exp, sqrt, pi, abs
import matplotlib.pyplot as plt

# %%
def wykres(l,r, wzor_string):
    x = np.arange(l, r, 0.01)
    y = eval(wzor_string)
    plt.title(f'Wykres {wzor_string}')
    plt.plot(x, y, linestyle='-')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.savefig("wykres.png")
    plt.show()

# %%
def calka(l,r,wzor_string,a,b):
    x = np.arange(l, r, 0.01)
    y = eval(wzor_string)
    plt.fill_between(x, y, where=[(i >= a and i <= b) for i in x], alpha=0.6, color='red')
    plt.title(f'Wykres {wzor_string} od {a} do {b}')
    plt.plot(x, y, linestyle='-')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.savefig("wykres.png")
    plt.show()

# %%
if __name__ == '__main__':
    print("Prosze podac operacje: 'wykres' lub 'całka'")
    op=input()
    print("Prosze podac lewy i prawy koniec dziedziny oraz wzor funkcji")
    l=float(input())
    r=float(input())
    x = np.arange(l, r, 0.01)
    wzor_string = input()
    if (op.lower()=='całka' or op.lower()=="calka"):
        print("Prosze podac lewy i prawy koniec przedzialu całkowania")
        a = float(input())
        b = float(input())
        calka(l,r,wzor_string,a,b)
    else:
        wykres(l,r,wzor_string)

# %% [markdown]
# jeśli funkcja jest całką to wykonujemy tą część kodu


