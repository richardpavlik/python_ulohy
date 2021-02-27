import math
def kvadraticka():
    a = int(input("Zadej první koeficient kvadratické rovnice: "))
    b = int(input("Zadej druhý koeficient kvadratické rovnice: "))
    c = int(input("Zadej třetí koeficient kvadratické rovnice: "))
    diskriminant = b**2 - 4*a*c
    if diskriminant < 0 :
        return None
    return f"První kořen je {(-b + math.sqrt(diskriminant)) / (2*a)}, druhý kořen je {(-b - math.sqrt(diskriminant)) / (2*a)}"

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


