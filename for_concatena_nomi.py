n= int(input("Quanti nomi vuoi inserire: "))
Elenco_Nomi=""
for i in range(0,n):
    nome= input("Inserisci il nome: ")
    Elenco_Nomi = Elenco_Nomi + "-" + nome
print(Elenco_Nomi.lstrip("-"))
    
