# Lien vers Github : https://github.com/MrBeepShow/bts-sio-python-tp1.git

def connexion(login, mot_de_passe):
    #Fonction de connexion
    essais_restants = 3
    while essais_restants > 1:
        if login == "admin" and mot_de_passe == "R@b13r123":
            return "Connexion réussie"
        else:
            essais_restants -= 1
            print(f"Identifiants incorrects. Il vous reste {essais_restants} essais.")
            login = input("\nLogin : ")
            mot_de_passe = input("Mot de passe : ")
    print("\n\n\n")
    return "Trop de tentatives échouées. Compte Bloqué."


def main():
     while True:
        login = input("Login : ")
        mot_de_passe = input("Mot de passe : ")
        resultat = connexion(login, mot_de_passe)
        print(resultat)

        if resultat == "Connexion réussie" or resultat == "Trop de tentatives échouées. Compte Bloqué.":
            break

if __name__ == "__main__":
   main()



