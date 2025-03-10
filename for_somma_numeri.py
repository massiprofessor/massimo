n=int(input("Quanti numeri vuoi sommare: "))
s=0
for i in range(0,n):
    numero= eval(input("Inserisci numero: "))
    s= s + numero
print("La somma è uguale a " + str(s))
