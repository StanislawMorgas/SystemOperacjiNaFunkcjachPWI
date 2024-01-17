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


print("Wybierz operacje:")