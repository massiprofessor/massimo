def somma(a,b):
    risultato= a + b
    return risultato

try:
    registro=[]
    numero=int(input("Inserisci numero: "))
    numero2= int(input("Inserisci numero: "))
    risultato=numero/numero2
    r= somma(numero,numero2)
    registro[0]=risultato
    print(r)
    
except ZeroDivisionError:
    print("Il secondo numero non può essere zero")
except ValueError:
    print("Dato non corretto")
except IndexError:
    print("L'indice non è esistente")
except TypeError:
    print("La funzione somma richiede n parametri")

    
