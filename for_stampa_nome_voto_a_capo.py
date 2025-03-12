s="Massimo-9-Annalisa-8-Fabio-10"
nome=""
voto=""
is_voto=False


for elem in s:
    if elem =="-":
        if is_voto==True:
            print(nome + "-" + voto)
            nome=""
            voto=""
        is_voto= not is_voto # nega quello che c'è nella variabile is_voto
    else:
        if is_voto==True:
            voto= voto + elem
        else:
            nome= nome + elem

print(nome + "-" + voto)
