

### IV. Exercices BONUS

def affiche_carres(n):
    for i in range(1, n+1):
        print(i**2)

def dessiner_carre(n):
    for i in range(n):
        print("* " * n)

def plus_grand_nombre():
    i = 0
    liste = []
    while i <3:
        try:
            nombre = (input("Entrez un nombre entier (ou tapez 'stop' pour terminer) : "))
            liste.append(int(nombre))
            i+=1
        except ValueError:
            print("Veuillez entrer un entier valide ou 'stop' pour terminer.")

    print(f"Le plus grand nombre entré est : {max(liste)}")

def trier_liste(liste):
    if not isinstance(liste, list):
        raise ValueError("L'argument doit être une liste.")
    for i in range(len(liste)):
        for j in range(len(liste)-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste




affiche_carres(10)
dessiner_carre(4)
plus_grand_nombre()
print(trier_liste([1, 5, 3, 9, 2]))


