#scrivere un programma che prende in input il nome di una squadra e pulisce
#il nome da imperfezioni



nome_sq= input("Inserire il nome della squadra: ")
#inter inter- -inter int er
nome_sq_corr=""
c=0
for elem in nome_sq:
    if elem != "-" and elem != " ":
        nome_sq_corr=nome_sq_corr + elem
    
    else:
        c=c+1
if c > 1:
    print("Ci sono",c,"errori")
elif c == 0:
    print("Non ci sono errori")
else:
    print("C'è 1 errore")
    
print(nome_sq_corr)

        
        
        
