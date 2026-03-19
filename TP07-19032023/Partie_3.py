

### III. Partie 3 : Parcourir des données 


def afficher_lettre(mot):
    for lettre in mot:
        print(lettre)

def compter_voyelles(mot):
    count = 0
    for lettre in mot:
        if lettre.lower() in "aeiouy":
            count += 1
    return count

def notes_valides(notes):
    list_notes_valides = []
    for note in notes:
        if note >= 10 :
            list_notes_valides.append(note)
    return list_notes_valides




afficher_lettre("Python")
print(compter_voyelles("bOnjour"))
print(notes_valides([12, 15, 9, 17, 8, 14]))
