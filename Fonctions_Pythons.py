#Exercice 1 – Fonction sans paramètre
def Dire_Bonjour():
    print("Bonjour BTS !")

#Exercice 2 – Fonction avec paramètre
def Saluer(nom):
    print(f"Bonjour {nom} !")

#Exercice 3 – Fonction avec calcul
def somme(a, b):
    return a + b

#Exercice 4 – Fonction + saisie utilisateur
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

