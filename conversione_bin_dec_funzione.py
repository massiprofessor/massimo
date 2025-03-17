def bindec(b):
    pot= len(b)-1
    dec=0
    for elem in b:
        if elem =="1":
            dec= dec + 2**pot
        pot=pot -1
    return dec




#"000" --> dec

binario=input("Inserisci binario da convertire: ")
decimale= bindec(binario)
print(decimale)
