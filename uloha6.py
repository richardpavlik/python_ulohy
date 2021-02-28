# tady pouzivam tzv. "list comprehension" a built-in funkci max()
def nejvetsi_zadana_cislo():
    return max([int(input("zadej číslo: ")) for i in range(5)])

