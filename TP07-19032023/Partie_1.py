import hashlib

### I. Partie 1 : Premières boucles while


def count_1_to_10():
        i = 1
        while i <= 10:
            print(i)
            i += 1

def count_10_to_1():
        i = 10
        while i >= 1:
            print(i)
            i -= 1

def sum_n(n):
        # Ne pas utiliser sum_n pour cet exercice faites appel à use_sum_n pour faire le lien entre les deux fonctions
        total = 0
        i = 1
        calc = ""
        while i <= n:
            total += i
            if i < n:
                calc += str(i) + "+"
            else:
                calc += str(i)
            i += 1
        return total,calc

def use_sum_n():
        while True:
            try:
                n = int(input("Entrez un nombre entier : "))
                break
            except ValueError:
                print("Veuillez entrer un entier valide.")
        total, calc = sum_n(n)
        print(f"Resultat : {total} ({calc})")


def password_check():
        password = input("Entrez votre mot de passe : ")
        while hashlib.sha256(password.encode()).hexdigest() != hashlib.sha256("python".encode()).hexdigest():
            print("Mot de passe incorrect. Essayez à nouveau.")
            password = input("Entrez votre mot de passe : ")
        print("Accès autorisé !")



count_1_to_10()
count_10_to_1()
use_sum_n()
password_check()