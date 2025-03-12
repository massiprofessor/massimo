import random
numero_segreto= random.randint(1,10)
tentativi=5
stato=False
while True:
    for i in range(tentativi):
        numero=int(input("Inserisci il numero da 1 a 10: "))
        if numero > numero_segreto:
            print("Troppo alto")
        elif numero < numero_segreto:
            print("Troppo basso")
        elif numero ==numero_segreto:
            print("Indovinato")
            break
            stato=True
    if stato == True or stato==False:
        break
            
