registro=""
#i voti sono da 0 a 9 
#"Massimo-6-Fabio-7"

while True:
    scelta= input("1. Per inserire nome e voto\n2. Visualizzare il voto di un nome\n3. Uscire\n\n")
    if scelta=="1":
        nomev=input("Inserisci nome e voto nel formatato nome-voto: ")
        #"Massimo-7"
        nomep= nomev.replace("-","")
        nomep= nomep.replace(nomep[-1],"")
        if nomep in registro:
            print("L'alunno esiste già")
        else:
            registro=registro + nomev + "-"
    elif scelta =="2":
        print(registro.rstrip("-"))
    elif scelta =="3":
        print("Ciao")
        break
            
        
        
