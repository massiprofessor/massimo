numero1=eval(input("Inserisci numero 1: "))
numero2=eval(input("Inserisci numero 2: "))
numero3=eval(input("Inserisci numero 3: "))

massimo= numero1

if numero2 > massimo:
    massimo= numero2
if numero3 > massimo:
    massimo= numero3

print("Il maggiore è",massimo)


