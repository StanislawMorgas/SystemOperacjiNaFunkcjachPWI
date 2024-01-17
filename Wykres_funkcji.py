# %%
import numpy as np
from numpy import cos, sin, log, exp, sqrt, pi, abs
import matplotlib.pyplot as plt

# %%
print("Prosze podac operacje: 'wykres' lub 'całka'")
op=input()
print("Prosze podac lewy i prawy koniec dziedziny oraz wzor funkcji")
l=float(input())
r=float(input())
x = np.arange(l, r, 0.01)
wzor=input()
y = eval(wzor)


# %% [markdown]
# jeśli funkcja jest całką to wykonujemy tą część kodu

# %%
plt.title(f'Wykres {wzor}')
if (op.lower()=='całka' or op.lower()=="calka"):
    print("Prosze podac lewy i prawy koniec przedzialu całkowania")
    a = float(input())
    b = float(input())
    plt.fill_between(x, y, where=[(i >= a and i <= b) for i in x], alpha=0.6, color='red')
    plt.title(f'Wykres {wzor} od {a} do {b}')
plt.plot(x, y, linestyle='-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
plt.savefig("wykres.png")


