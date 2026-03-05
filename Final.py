def stockList():
    Lstock = []
    for i in range(1, 6):
        while True:
            try:
                a = float(input(f"Nombre {i} : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        Lstock.append(a)
    for i in range(len(Lstock)):
        if Lstock[i].is_integer():
            Lstock[i] = int(Lstock[i])
    Lstock.sort()    
    return Lstock

print(stockList())