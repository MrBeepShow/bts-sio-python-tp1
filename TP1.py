# Lien vers Github : https://github.com/MrBeepShow/bts-sio-python-tp1.git

from ast import main
from hashlib import sha256

def exercice_1():
    #le Début
    while True:
        try:
            age = int(input("Quel est votre âge ? "))
            if age < 0:
                print("L'âge ne peut pas être négatif. Veuillez réessayer.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour l'âge.")            
    if age < 18:
        print("Vous êtes mineur.")
    else:
        print("Vous êtes majeur.")

def exercice_2():
    #Comparaison de nombres
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
    #Vérification de mot de passe
    while True:
        mot_de_passe = input("Entrez un mot de passe : ")
        if len(mot_de_passe) < 8:
            print("Le mot de passe est trop court. Il doit contenir au moins 8 caractères.")
        else:
            break
    # Suite à un retour des étudiants de BTS SIO 2, le mot de passe correct est : R@bi3r123*%
    temoin = sha256("R@bi3r123*%".encode()).hexdigest()
    # On compare le hash du mot de passe entré avec le hash du mot de passe correct
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

def exercice_5():
    #Pair ou impair
    while True:
        try:
            nombre = int(input("Entrez un nombre entier : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    if nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

def exercice_6():
    #Accès à une attraction
    while True:
        try:
            age = int(input("Quel est votre âge ? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour l'âge.")

    while True:
        try:
            taille = float(input("Quelle est votre taille en cm ? "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour la taille.")

    if age >= 12 and taille >= 140:
        print("Accès Autorisé.")
    else:
        print("Accès Refusé.")

def est_majeur(age):
   #Fonction de majorité        
    if age >= 18:
        return True
    else:
        return False

def tarif(age):
    #Fonction de tarif
    if age < 12:
        return "Enfant"
    elif age < 18:
        return "Adolescent"
    elif age < 65:
        return "Adulte"
    else:
        return "Senior"
    
def calculateur(nombre1, nombre2, operateur):
    #Fonction de calculatrice
    if operateur == "+":
        return nombre1 + nombre2
    elif operateur == "-":
        return nombre1 - nombre2
    elif operateur == "*":
        return nombre1 * nombre2
    elif operateur == "/":
        if nombre2 != 0:
            return nombre1 / nombre2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opération non reconnue"

def connexion(login, mot_de_passe):
    #Fonction de connexion
    temoin_login = "root"
    temoin_mot_de_passe = sha256("!!_Ca_C_pYthon_**".encode()).hexdigest()
    if login == temoin_login and sha256(mot_de_passe.encode()).hexdigest() == temoin_mot_de_passe:
        return "Connexion réussie"          
    elif login != temoin_login and sha256(mot_de_passe.encode()).hexdigest() == temoin_mot_de_passe:
        return "Connexion échouée : Login incorrect"
    elif login == temoin_login and sha256(mot_de_passe.encode()).hexdigest() != temoin_mot_de_passe:
        return "Connexion échouée : Mot de passe incorrect"
    else:
        return "Connexion échouée : Identifiants incorrects"



if __name__ == "__main__":
    exercice_1()
    exercice_2()
    exercice_3()
    exercice_4()
    exercice_5()
    exercice_6()