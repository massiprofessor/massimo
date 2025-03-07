scelta=input("1. per add\n2. per sott\n3. per mol\n4. per div\n\n")
numero=eval(input("Inserici numero: "))
numero2= eval(input("Inserici numero: "))
stato=False
if scelta=="1":
    risultato= numero + numero2
    stato=True
elif scelta=="2":
    risultato=numero - numero2
    stato=True
elif scelta=="3":
    risultato=numero * numero2
    stato=True
elif scelta=="4" and numero2 != 0:
    risultato=numero / numero2
    stato=True

if stato== True:
    print(risultato)
else:
    print("Operazione di divisione per zero non si puà fare")
