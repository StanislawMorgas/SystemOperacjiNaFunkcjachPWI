from time import sleep
from Wykres_funkcji import calka, wykres
from input import *
from calka_monte_carlo import *
from calka_num import *

def wybierzFunkcje(lista):
    while True:
        try:
            a = int(input("Podaj indeks funkcji która chesz użyć (Zaczynając od 1): "))
            if a > 0 and a <= len(lista):
                return a-1
            else:
                print("Wpisano niepoprawny argument")
        except ValueError:
            print("Wpisano niepoprawny argument")

def wybierzZakres(c):
    while True:
        try:
            if c:
                a = int(input("Podaj lewy zakres wykresu: "))
                break
            else:
                a = int(input("Podaj lewy zakres całki: "))
                break
        except ValueError:
            print("Wpisano niepoprawny argument")
    while True:
        try:
            if c:
                b = int(input("Podaj prawy zakres wykresu: "))
            else:
                b = int(input("Podaj prawy zakres całki: "))
            if b < a:
                print("Podano błędny zakres.")
            else: return a,b
        except ValueError:
            print("Wpisano niepoprawny argument")

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
    6. Dodaj funkcje do listy
    7. Zapisz funkcje do pliku
    8. Zakończ
    """)
    try:
        a = int(input("Wpisz numer operacji: "))
    except ValueError:
        print("Wpisano niepoprawny argument")
        print()
        print("-----------------------------------------------------------")
        continue

    if a == 1:
        czy_wczytane = True
        funk = wczytaj()
    elif a == 2:
        if czy_wczytane:
            wybor = parsujDoObliczen(funk[wybierzFunkcje(funk)])
            a,b = wybierzZakres(False)
            try:
                print(f"Wynik: {calka_monte_carlo(wybor,a,b)}")
            except TypeError:
                print("Podana funkcja jest niepoprawna.")
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 3:
        if czy_wczytane:
            wybor = parsujDoObliczen(funk[wybierzFunkcje(funk)])
            a, b = wybierzZakres(False)
            try:
                print(f"Wynik: {calka_num(wybor,a,b)}")
            except NameError:
                print("Podana funkcja jest niepoprawna.")
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
            wybor = parsujDoObliczen(funk[wybierzFunkcje(funk)])
            a, b = wybierzZakres(True)
            if "^" in list(wybor):
                wybor = wybor.replace("^", "**")
            try:
                wykres(a,b,wybor)
                print('Wykres został wygenerowany do pliku "wykres.png".')
            except NameError:
                print("Podana funkcja jest niepoprawna")
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 6:
        if czy_wczytane:
            funk.append("y = " + input("Podaj wzór funkcji, y = "))
    elif a == 7:
        if czy_wczytane:
            zapisz(funk)
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 8:
        print("Miłego dnia :)")
        exit()
    else:
        print("Wpisano niepoprawny argument")
    print()
    print("-----------------------------------------------------------")

r"""
 ___________________________________ 
< Pamiętajcie o 8 godzinach snu :) >
 ----------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

