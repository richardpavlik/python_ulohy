import random
def nahodne_cislo():
    tajne_cislo = random.choice(range(1, 10))
    print(tajne_cislo)
    print("Zkus uhádnout číslo od 1 do 9, máš na to pouze tři pokusy!")
    pokusy = 3
    while pokusy > 0:
        x = int(input("Zadej číslo: "))
        if x == tajne_cislo:
            return "Uhádnul/a si číslo!"
        pokusy -=1
        if pokusy > 0:
            print(f"Ještě máš tolik pokusů: {pokusy}")
        else:
            return "Prohrál/a si!"


#verze s try except - když hráč zadá něco jiného než číslo, program nespadne, ale vypíše zprávu a spustí se znova
"""
import random
def nahodne_cislo():
    tajne_cislo = random.choice(range(1, 10))
    print("Zkus uhádnout číslo od 1 do 9, máš na to pouze tři pokusy!")
    pokusy = 3
    while pokusy > 0:
        try:
            x = int(input("Zadej číslo: "))
            if x == tajne_cislo:
                return "Uhádnul/a si číslo!"
            pokusy -=1
            if pokusy > 0:
                print(f"Ještě máš tolik pokusů: {pokusy}")
            else:
                print("Prohrál/a si!")
        except ValueError:
            print("Zadej platné číslo!")
"""
