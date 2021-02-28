import math
def kvadraticka():
    a = float((input("Zadej první koeficient kvadratické rovnice: ")))
    b = float((input("Zadej druhý koeficient kvadratické rovnice: ")))
    c = float((input("Zadej třetí koeficient kvadratické rovnice: ")))
    if a == 0 or b == 0 or c == 0:
        return "Koeficient se nesmí rovnat nule!"
    diskriminant = b**2 - 4*a*c
    if diskriminant < 0 :
        return "Dikriminant je menší než nula, zadej jiné koeficienty."
    print(f"Dikriminant je: {diskriminant}")
    print(f"Kvadratická rovnice vypadá takto: {a}x2 + {b}x + {c}")
    return f"První kořen je {(-b + math.sqrt(diskriminant)) / (2*a)}, druhý kořen je {(-b - math.sqrt(diskriminant)) / (2*a)}"
#f značí tzv. "formatted string"

"""
Verze s try a except

import math
def kvadraticka():
    try:
        a = int(input("Zadej první koeficient kvadratické rovnice: "))
        b = int(input("Zadej druhý koeficient kvadratické rovnice: "))
        c = int(input("Zadej třetí koeficient kvadratické rovnice: "))
        diskriminant = b**2 - 4*a*c
        if diskriminant < 0 :
            return None
        return f"První kořen je {(-b + math.sqrt(diskriminant)) / (2*a)}, druhý kořen je {(-b - math.sqrt(diskriminant)) / (2*a)}"
    except ValueError:
        return "Zadej platné koeficienty kvadratické rovnice!"

"""


