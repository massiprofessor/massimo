def nome():
    nomi=""
    for i in range(3):
        nome=input("Inserisci nome: ")
        nomi=nomi + nome
        yield nomi

for nomi in nome():
    print(nomi)


#yield restituisce e congela il valore di una funzione permettendo di usare una
#funzione come generatore di valori iterabile
        
