

### II. Partie 2 : Boucles for 

def afficher_nombres(n):
        for i in range(n + 1):
            print(i)


def table_mult(nombre):
    for i in range(11):
        print(f"{nombre} x {i} \t= \t{nombre * i}")

def somme_nombre(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


afficher_nombres(5)
table_mult(3)
print(somme_nombre(10))