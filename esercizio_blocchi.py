nb= int(input("Inserisci numero di blocchi: "))
altezza,livello,costruzione=0,0,0
while costruzione <= nb and nb != 0:
    altezza=livello
    livello= livello+1
    costruzione= costruzione + livello
print("Altezza",altezza)
