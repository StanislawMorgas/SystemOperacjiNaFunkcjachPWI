import json

def zapisz(L):
    """Przyjmuje liste funkcji i zapisuje ją do pliku funkcje.json"""
    funkcje_data = {"funkcje": L}
    with open('funkcje.json', 'w') as file:
        json.dump(funkcje_data, file, indent=4)
    print("Funkcje zostały zapisane do pliku 'funkcje.json'.")
    print("Miłego dnia :)")

"""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) 
"""

def wczytaj():
    """Zwraca liste funkcji z pliku funkcje.JSON"""
    with open('funkcje.json', 'r') as file:
        data = json.load(file)
    funkcje_lista = data['funkcje']
    print("Funkcje zostały wczytane.")
    print("Miłego dnia :)")
    return funkcje_lista

