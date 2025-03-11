#Scrivere un programma che individua quali sono le vocali e consonanti
#in una stringa presa in input e quante sono le vocali e consonanti trovate


nome=input("Inserisci stringa: ")
vocali="aeiou"
vocali_trovate=""
consonanti_trovate=""
for elem in nome:
    #ciao
    if elem in vocali:
        vocali_trovate=vocali_trovate + elem
    else:
        consonanti_trovate= consonanti_trovate + elem
print("Vocali individuate:",vocali_trovate,"Quantità:",len(vocali_trovate))
print("Consonanti individuate:",consonanti_trovate,"Quantità:",len(consonanti_trovate))
    
        
        
        
