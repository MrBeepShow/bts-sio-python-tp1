#Ce Programme est le jeu du Nombre Mystere
import random
def jeu_nombre_mystere():
    nombre_mystere = random.randint(1, 10)
    print("Bienvenue dans le jeu du Nombre Mystère !")
    print("Je pense à un nombre entre 1 et 10. Pouvez-vous le deviner ?")

    while True:
        try:
            guess = int(input("Entrez votre proposition : "))
            if guess < 1 or guess > 10:
                print("Veuillez entrer un nombre entre 1 et 10.")
                continue
            if guess < nombre_mystere:
                print("C'est plus !")
            elif guess > nombre_mystere:
                print("C'est moins !")
            else:
                print("Félicitations ! Vous avez trouvé le nombre mystère !")
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    jeu_nombre_mystere()