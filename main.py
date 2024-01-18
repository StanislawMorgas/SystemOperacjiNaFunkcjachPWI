from time import sleep
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

def wybierzZakres():
    while True:
        try:
            a = int(input("Podaj lewy zakres całki: "))
            break
        except ValueError:
            print("Wpisano niepoprawny argument")
    while True:
        try:
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
    6. Zapisz funkcje do pliku
    7. Zakończ
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
            a,b = wybierzZakres()
            print(f"Wynik: {calka_monte_carlo(wybor,a,b)}")
        else:
            print("Funkcje nie zostały wczytane")
    elif a == 3:
        if czy_wczytane:
            wybor = parsujDoObliczen(funk[wybierzFunkcje(funk)])
            a, b = wybierzZakres()
            print(f"Wynik: {calka_num(wybor,a,b)}")
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

