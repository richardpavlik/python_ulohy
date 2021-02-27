# list (seznam) je jedna z tzv. data structures v pythonu
a = ['pes', 'kočka', 'králík', 'had']

# tímto řádkem kódu definujeme funkci
# v závorkách jsou atributy, které ve funkci používáme, přesně je ale určíme až když funkci "zavoláme"
def hledej(slovo, seznam):
    #tento řádek zkoumá jestli je daná proměnná (v tomto případě slovo) obsažena v jiné proměnné (v tomto případě v seznamu)
    if slovo in seznam:
    #funkce nám vrátí tzv "boolean" hodnotu, v tomto případě True
        return True
    #pokud žádná z předchozích podmínek nebyla splněna aktivuje se tato
    else: 
    #funkce nám vrátí tzv "boolean" hodnotu, v tomto případě False
        return False

#proměnná, kterou použiji ve while loop
run = True
#pokud je daná podmínka platná (je True / Truthy (není to prázdná proměnná nebo nula)), while loop se bude opakovat
while run:
    #input, který dále použijeme, built-in (vestavěnou) funkcí .lower(), převedeme na malá písmena pro snadnější použití
    zvire = input('Napiš nějaké zvíře: ').lower()
    #tento řádek zkoumá, zda-li naše funkce vrátila True
    if hledej(zvire, a) == True:
        #pokud je tato podmínka splněna, aktivuje se následující řádek kódu, který do terminálu vypíše danou větu
        print('Zvíře, které jsi zadal/a, patří do seznamu.')
    #pokud žádná z předchozích podmínek nebyla splněna aktivuje se tato
    else:
        #do terminálu se vypíše následující věta
        print('Zvíře, které jsi zadal/a, nepatří do seznamu.')

    #input, který použijeme, pokud chce hráč hrát znova    
    otazka = input("Chceš hrát znova? (y/n) ")
    #zkoumá jestli je input roven "n" (hráč už nechce hrát)
    if otazka.lower() == "n":
        #pokud je daná podmínka splněna, program do konzole vypíše následující větu
        print("Nashledanou!")
        #pokud je daná podmínka splněna, proměnnou, která slouží jako podmínka ve while loop, stanovíme na hodnotu False, a tudíž se while loop zastaví
        run = False
    #else psát nemusíme, protože když hráč napíše "y", proměnná run bude pořád na hodnotě True