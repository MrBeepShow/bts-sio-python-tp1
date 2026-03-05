#  Exercice 1 : Afficher du texte 
print("Hello World !")

# Exercice 2 : Interaction utilisateur 
print(f"Vous avez écris : \"{input("Insérez quelque chose : ")}\"")

# Exercice 3 : Calcul simple (somme)
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

#Exercice 4 : Autres exemples simples 
#Moyenne de deux nombres
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

#Conversion cfp → euros : 
while True:
    try:
        cfp = int(input("Montant en CFP : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")
euro = cfp / 119.33
print(f"{cfp} CFP équivaut à {euro:.2f} Euros.")
#Conversion euros → cfp : 
while True:
    try:
        euro = float(input("Montant en Euros : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        
cfp = int(euro * 119.33)
print(f"{euro} Euros équivaut à {cfp} CFP.")