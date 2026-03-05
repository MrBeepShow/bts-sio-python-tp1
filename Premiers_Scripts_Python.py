def affichage():
    print("Hello World !")

def Entrée():
    print(f"Vous avez écris : \"{input("Insérez quelque chose : ")}\"")

def Calcul():
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
    print("Le résultat de l'addition est : ", a + b)

def CalculFloat():
    while True:
        try:
            a = float(input("Nombre 1 : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    while True:
        try:
            b = float(input("Nombre 2 : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    print("La moyenne est : ", (a + b) / 2)

def Conversion_CfpToEuro():
    while True:
        try:
            cfp = float(input("Montant en CFP : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    euro = cfp / 119.33
    print(f"{cfp} CFP équivaut à {euro:.2f} Euros.")

def Conversion_EuroToCfp():
    while True:
        try:
            euro = float(input("Montant en Euros : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    cfp = euro * 119.33
    print(f"{euro} Euros équivaut à {cfp} CFP.")



