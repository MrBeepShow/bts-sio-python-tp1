#Ce programme calcule le prix final d'un produit après application d'une remise
def calculer_prix_final(prix_initial, remise):
    if remise < 0 or remise > 100:
        print("La remise doit être comprise entre 0 et 100.")
        return None
    prix_final = prix_initial * (1 - remise / 100)
    return prix_final

def main():
    while True:
        try:
            prix_initial = float(input("Entrez le prix initial du produit : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour le prix initial.")
    while True:
        try:
            remise = float(input("Entrez le pourcentage de remise : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour la remise.")
    
    prix_final = calculer_prix_final(prix_initial, remise)
    if prix_final is not None:
        print(f"Le prix final après application de la remise est : {prix_final:.2f}")

if __name__ == "__main__":
    main()