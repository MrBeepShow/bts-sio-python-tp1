from hashlib import sha256

def demande_age():
    while True:
        try:
            age = int(input("Quel est votre âge ? "))
            if age < 0:
                print("L'âge ne peut pas être négatif. Veuillez réessayer.")
            else:
                return age
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour l'âge.")


def exercice_1():
    age = demande_age()
    if age < 18:
        print("Vous êtes mineur.")
    else:
        print("Vous êtes majeur.")

def exercice_2():
    nombre = input("Entrez un nombre : ")
    while True:
        try:   
            nombre = float(nombre)
            break
        except ValueError:
            print("Ce n'est pas un nombre valide.")
            nombre = input("Entrez un nombre : ")
    if nombre < 0:
        print("Le nombre est négatif.")
    elif nombre > 0:
        print("Le nombre est positif.")
    else:  
        print("Le nombre est égal à zéro.")

def exercice_3():
    while True:
        mot_de_passe = input("Entrez un mot de passe : ")
        if len(mot_de_passe) < 8:
            print("Le mot de passe est trop court. Il doit contenir au moins 8 caractères.")
        else:
            break
    # Suite à un retour des étudiants de BTS SIO 2, le mot de passe correct est : R@bi3r123*%
    temoin = sha256("R@bi3r123*%".encode()).hexdigest()
    if sha256(mot_de_passe.encode()).hexdigest() == temoin:
        print("Accès autorisé.")
    else:
        print("Accès refusé.")

def exercice_4():
    #Calcul de moyenne
    while True:
        try:
            note = float(input("Entrez votre note : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour la note.")
    if note >= 16:
        print("Très bien !")
    elif note >= 14:
        print("Bien !")
    elif note >= 12:
        print("Assez bien !")
    elif note >= 10:
        print("Passable !")
    else:
        print("Ajourné !")

if __name__ == "__main__":
    exercice_1()
    exercice_2()
    exercice_3()
    exercice_4()
