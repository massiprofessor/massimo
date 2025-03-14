nomi=[]
for i in range(3):
    nome=input("Inserisci nome nella lista: ")
    nomi.append(nome)

#visulizza la lista per elemento

nomi_view=""
for elem in nomi:
    nomi_view= nomi_view + "-" + elem
print(nomi_view.lstrip("-"))

