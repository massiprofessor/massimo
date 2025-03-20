numeri=[1,2,3,4,5]
numeri= list(map(lambda x: x**2, numeri))
print(numeri)

#list inserisci in una lista
#map richiede il primo argomento una funzione, il secondo argomento input
#lambda permette di creare una funzione al volo dove in questo caso
#ogni elemento dell'input passa alla variabile x


#Esempio 2


numeri=[1,2,3,4,5]
numeri=list(filter(lambda x: x%2 == 0,numeri))
print(numeri)

#filter vuole 2 argomenti, funzione con condizione, input

