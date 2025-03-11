nv= int(input("Inserisci quanti numeri vuoi analizzare: "))
risultato=""
for i in range(nv):
    numero=int(input("Inserisci numero da analizzare: "))
    if numero % 2 == 0:
        
        risultato= risultato + str(numero) + " "*(12-len(str(numero))) + str(numero**2) + "\n"
print("Numero pari-Quadrato")
print(risultato)
