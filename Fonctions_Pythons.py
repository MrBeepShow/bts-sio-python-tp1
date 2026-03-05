def Dire_Bonjour():
    print("Bonjour BTS !")

def Saluer(nom):
    print(f"Bonjour {nom} !")

def somme(a, b):
    return a + b

def sommeUI():
    while True:
        try:
            a = int(input("Nombre 1 : "))
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")
    while True:
        try:
            b = int(input("Nombre 2 : "))
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")
    print("Le résultat de l'addition est : ", somme(a, b))

def stockList():
    Lstock = []
    for i in range(1, 6):
        while True:
            try:
                a = float(input(f"Nombre {i} : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        Lstock.append(a)
    for i in range(len(Lstock)):
        if Lstock[i].is_integer():
            Lstock[i] = int(Lstock[i])
    Lstock.sort()    
    return Lstock

print(stockList())