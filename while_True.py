while True:
    scelta=input("1. per concatenare\n1. per sommare\n3. per uscire\n\n")
    if scelta=="1":
        nomi=""
        for i in range(3):
            nome=input("Inserisci nome: ")
            nomi=nomi + nome
        print(nomi)
    if scelta=="2":
        s=0
        numero=0
        while numero >= 0:
            numero= int(input("Inserisci numero o numero negativo per uscire: "))
            if numero >= 0:
                s= s + numero
        print(s)
    if scelta=="3":
        print("Arrivederci e grazie")
        break
            
