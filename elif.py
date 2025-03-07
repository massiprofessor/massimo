scelta=input("1. per add\n2. per sott\n3. per mol\n\n")
numero=eval(input("Inserici numero: "))
numero2= eval(input("Inserici numero: "))
if scelta=="1":
    risultato= numero + numero2
elif scelta=="2":
    risultato=numero - numero2
elif scelta=="3":
    risultato=numero * numero2
print(risultato)
    
