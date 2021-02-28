a = int(input("Zadej číslo a: "))
b = int(input("Zadej číslo b: "))
op = input("Vyber operátor z nabídky +, -, *, / :   ")
if b == 0 and op == "/":
    print("Nemůžeš dělit nulou!\nZadej buď jiné číslo nebo operátor!")
    b = int(input("Zadej číslo b: "))
    op = input("Vyber operátor z nabídky +, -, *, / :   ")
print("Zvolil jsi operaci",op)
if op == "+":   
    vysl = a + b
elif op == "-": 
    vysl = a - b
elif op == "*": 
    vysl = a * b
else:   
    vysl = a/b
print(a, op, b, "=", vysl)

