from input import *
from time import sleep

logo = r"""
 ________  ________  ________   ________ 
|\   ____\|\   __  \|\   ___  \|\  _____\
\ \  \___|\ \  \|\  \ \  \\ \  \ \  \__/ 
 \ \_____  \ \  \\\  \ \  \\ \  \ \   __\
  \|____|\  \ \  \\\  \ \  \\ \  \ \  \_|
    ____\_\  \ \_______\ \__\\ \__\ \__\ 
   |\_________\|_______|\|__| \|__|\|__| 
   \|_________|                           ©

System operacji na funckjach - projekt na PWI
"""
for linijka in logo.splitlines():
    print(linijka)
    sleep(0.2)

czy_wczytane = False

while True:
    if czy_wczytane:
        print("Wczytane funkcje:")
        print(funk)
        print()
    print("""Wybierz operacje:
    1. Załaduj funkcje z pliku
    2. Oblicz całke (Metoda Monte Carlo)
    3. Oblicz całke (Numerycznie)
    4. Uprość funkcje
    5. Narysuj wykres funkcji
    6. Zapisz funkcje do pliku
    7. Zakończ
    """)
    try:
        a = int(input("Wpisz numer operacji: "))
    except ValueError:
        print("Wpisano niepoprawny argument")
        print("-----------------------------------------------------------")
        continue

    if a == 1:
        czy_wczytane = True
        funk = wczytaj()
    elif a == 2:
        if czy_wczytane:
            #tu coś do liczenia calek monte carlo
            #tu powinien być prompt o wpisanie indexu funkcji w liscie ktorej chcemy uzyc i ta funkcja powinna byc przekazana do odpowiedniej funkcji
            #reszta opcji analogicznie
            pass
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 3:
        if czy_wczytane:
            #tu cos do liczenia calek numerycznie
            pass
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 4:
        if czy_wczytane:
            #tu cos do uproszczenia funkcji
            pass
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 5:
        if czy_wczytane:
            #tu cos do rysowania wykresow
            pass
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 6:
        if czy_wczytane:
            zapisz(funk)
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 7:
        print("Miłego dnia :)")
        exit()
    else:
        print("Wpisano niepoprawny argument")
    print("-----------------------------------------------------------")

