nv= int(input("Inserisci quanti numeri vuoi analizzare: "))
for i in range(nv):
    numero=int(input("Inserisci numero da analizzare: "))
    if numero % 2 == 0:
        print("Il numero",numero,"è pari e il suo quadrato è",numero**2)
    
