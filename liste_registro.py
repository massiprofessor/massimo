registro=[]

# [["Nome","Voti"],["Nome","Voti"]]


while True:
    scelta=input("1.Per inserire nomi\n2. Per inserire voti\n3. Visualizzare voti\n4. Uscire\n\n")
    if scelta=="1":
        nomi=input("Inserisci nomi da inserire nel registro: ")
        #Massimo-Fabio
        nomi= nomi.split("-")
        #["Massimo","Fabio"]
        if len(registro) == 0:
            for elem in nomi:
                registro.append([elem])
        else:
            for e in nomi:
                trovato=False
                for i in range(len(registro)):
                    if e in registro[i]:
                        trovato=True
                        break
                if trovato==False:
                    registro.append([e])
            print(registro)
    if scelta=="2":
        nome=input("A chi vuoi aggiungere il voto: ")
        trovato=False
        for i in range(len(registro)):
            if nome in registro[i]:
                trovato=True
                indice=i
                break
        if trovato==True:
            voti=input("Inserisci i voti: ")
            voti= voti.split("-")
            #[["Massimo"]]
            for v in voti:
                registro[indice].append(v)
        else:
            print("Nome inesistente")
        print(registro)
    if scelta == "3":
        #Nomi ---------- Voti
        spazio=16
        #[["Massimo","7","6"]]
        print("Nomi ---------- Voti")
        for elem in registro:
            vo=""
            for i in range(0,len(elem)):
                if i==0:
                    continue
                else:
                    vo=vo + "-" + elem[i]
            print(elem[0] + " " *(spazio-len(elem[0])) + vo.lstrip("-"))
    if scelta =="4":
        print("Arrivederci")
        break
        
                


                
                        
                        
                
    
