
from random import *

vstup = input("\nVítejte v nejlepší hře světa \nJá si budu myslet číslo od 1 do 10 a ty ho musíš uhodnout \nZvolte obtížnost L-Lehké, T-Těžké: ")
cislo = randint(1,10)
znak = False

if vstup == "l" or vstup == "L":

    while True:
        tip = input(f"\nZvolil jste Lehkou obtížnost (myslím si {cislo}) \nHádejte: ")

        try:
            tip = int(tip)
        except ValueError:
            print("Víš vůbec co znamená číslo? Nebo tě to maminka nenaučila? Nebo seš Mr. Zhou?")
            znak = True

        if tip == cislo:
            print("Skvěle uhodl jste číslo")
            break

        elif not znak:
            print("Naskytl se problém. Zkuste to prosím později")
            break




elif vstup == "t" or vstup == "T":
    while True:
        tip = input(f"\nZvolil jste Těžkou obtížnost \nHádejte: ")

        try:
            tip = int(tip)
        except ValueError:
            print("Víš vůbec co znamená číslo? Nebo tě to maminka nenaučila? Nebo seš Mr. Zhou?")
            znak = True

        if tip == cislo:
            print("Skvěle uhodl jste číslo")
            break

        elif not znak:
            print("Naskytl se problém. Zkuste to prosím později")
            break
else:
    pass