nome=input("Inserisci nome: ")
vocali="aeiou"
#ciao
for elm in nome:
    if elm in vocali:
        print(elm)
        break
