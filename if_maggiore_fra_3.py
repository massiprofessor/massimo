n1=eval(input("Inserisci numero 1: "))
n2=eval(input("Inserisci numero 2: "))
n3=eval(input("Inserisci numero 3: "))
stato=False
if n1==n2 and n1 == n3:
    print("Tutti i numeri sono uguali")
    stato=True
else:
    max=n1
    min=n1
    if n2>max:
        max=n2
    else:
        min=n2
    if n3 > max:
        max=n3
    else:
        min=n3
if stato==False:
    print("Il massimo è",max)
    print("Il minimo è",min)
