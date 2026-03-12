#Ce programme vérifie si un mot de passe suit les critères de sécurité
def valide_mdp(mdp):
    if len(mdp) < 12:
        return False
    if not any(char.isupper() for char in mdp):
        return False
    if not any(char.isdigit() for char in mdp):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in mdp):
        return False
    return True

def main():
    while True:
        mdp = input("Entrez un mot de passe : ")
        if valide_mdp(mdp):
            print("Mot de passe valide.")
            break
        else:
            print("Mot de passe trop faible. Il doit contenir au moins 12 caractères, une majuscule, un chiffre et un caractère spécial.")

if __name__ == "__main__":
    main()