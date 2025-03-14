registro = []
while True:
    nomi=input("Nomi: ")
    nomi= nomi.split("-")

# Aggiungo solo i nomi non presenti
    for nome in nomi:
        trovato=False
        for i in range(len(registro)):
            if nome in registro[i]:
                trovato=True
                break
        if trovato==False:
            registro.append([nome])
            
       

# Stampa il registro aggiornato
    print(registro)
