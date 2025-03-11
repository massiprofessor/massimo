nome_cognome=input("Inserisci nome e cognome: ").lower()
nome=""
cognome=""
if " " in nome_cognome:
    stato_nome=False #Falso per il nome True per il cognome
    for elem in nome_cognome:
        #"massimo mezzina"
        #elem="m"
        if elem != " " and stato_nome == False :
            nome= nome + elem
        else:
            stato_nome=True
        if elem != " " and stato_nome == True:
            cognome= cognome + elem
    print("Il nome è",nome)
    print("Il cognome è",cognome)
else:
    print("Nome e cognome in input non sono formattati correttamente")

            
            
    
